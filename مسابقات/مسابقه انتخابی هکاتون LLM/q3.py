# Score of 60 during the contest


from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset
from sklearn.metrics import accuracy_score
import nltk
from nltk.corpus import wordnet
import random

df = pd.read_csv('/mnt/data/train.csv')
df['labels'] = df['category'].map({'Applied': 0, 'ML': 1})
train_df, val_df = train_test_split(df, test_size=0.1)
train_ds = Dataset.from_pandas(train_df)
val_ds = Dataset.from_pandas(val_df)
tok = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

def prep_func(ex):
    tok_ex = tok(ex['abstract'], padding="max_length", truncation=True)
    tok_ex['labels'] = ex['labels']
    return tok_ex

train_ds = train_ds.map(prep_func, batched=True)
val_ds = val_ds.map(prep_func, batched=True)
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)
train_args = TrainingArguments(
    output_dir='./results', num_train_epochs=3, per_device_train_batch_size=8,
    per_device_eval_batch_size=8, warmup_steps=500, weight_decay=0.01,
    logging_dir='./logs', evaluation_strategy="steps", eval_steps=50,
)

def comp_metrics(pred):
    return {'accuracy': accuracy_score(pred.label_ids, pred.predictions.argmax(-1))}

trainer = Trainer(model=model, args=train_args, train_dataset=train_ds, eval_dataset=val_ds, compute_metrics=comp_metrics)
trainer.train()
trainer.evaluate()

nltk.download('wordnet')
nltk.download('omw-1.4')

def syn_rep(word):
    syns = {lem.name().replace("_", " ").replace("-", " ").lower() for syn in wordnet.synsets(word) for lem in syn.lemmas()}
    syns.discard(word)
    return random.choice(list(syns)) if syns else word

def aug_sent(sent, n=3):
    words = sent.split()
    return ' '.join(syn_rep(word) if word in random.sample(words, min(n, len(words))) else word for word in words)

df['aug_abstract'] = df['abstract'].apply(aug_sent, n=3)
df = pd.concat([df[['abstract', 'category']].rename(columns={'abstract': 'text'}), df[['aug_abstract', 'category']].rename(columns={'aug_abstract': 'text'})], ignore_index=True)
df['labels'] = df['category'].map({'Applied': 0, 'ML': 1})
train_df, val_df = train_test_split(df, test_size=0.1, random_state=42)
train_ds = Dataset.from_pandas(train_df)
val_ds = Dataset.from_pandas(val_df)

def tok_func(ex):
    return tok(ex['text'], padding="max_length", truncation=True)

train_ds = train_ds.map(tok_func, batched=True)
val_ds = val_ds.map(tok_func, batched=True)
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)
train_args.num_train_epochs = 4
trainer = Trainer(model=model, args=train_args, train_dataset=train_ds, eval_dataset=val_ds, compute_metrics=lambda p: {'accuracy': (p.predictions.argmax(-1) == p.label_ids).astype(float).mean()})
trainer.train()
print(trainer.evaluate())

test_df = pd.read_csv('/mnt/data/test.csv')
test_ds = Dataset.from_pandas(test_df).map(lambda ex: tok(ex['abstract'], padding="max_length", truncation=True), batched=True)
preds = trainer.predict(test_ds)
pred_cats = [list({'Applied': 0, 'ML': 1}.keys())[list({'Applied': 0, 'ML': 1}.values()).index(l)] for l in preds.predictions.argmax(-1)]
output_df = pd.DataFrame({'prediction': pred_cats})
output_csv_path = '/mnt/data/output.csv'
output_df.to_csv(output_csv_path, index=False)