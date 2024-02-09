import pandas as pd

quesDF = pd.read_csv('qoura_questions.csv')
sherDF = pd.read_csv("shereno.csv")

# q1
summation = 0
for ques in quesDF['question']:
    summation += len(set(ques.split()))
print(summation)

# q2
sumDigitQues = sum(sum(c.isdigit() for c in ques) for ques in quesDF["question"])
sumDigitSher = sum(sum(c.isdigit() for c in poem) for poem in sherDF["Poem"])
print(sumDigitQues, sumDigitSher)

# q3
with open('stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set(file.read().splitlines())
sumStop = sum(sum(word in stopwords for word in poem.lower().split()) for poem in sherDF["Poem"])
print(sumStop)