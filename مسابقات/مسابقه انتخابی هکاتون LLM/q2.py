# Q3 and Q4 not accepted

from collections import Counter
import pandas as pd
import re

quesDF = pd.read_csv('qoura_questions.csv')

# q1
count = 0
for ques in quesDF['question']:
    ques = ques.lower().strip()
    for c in ",.!?:;''\"()[]}{}":
        ques = ques.replace(c, '')
    words = ques.split()
    for w in words:
        if len(w) > 4 and w[0] == 'm' and w[-1] == 't':
            count += 1
print(count)

# q2
pattern = re.compile(r"[\U0001F600-\U0001F9FF\U0001FA00-\U0001FA6F\U0001F700-\U0001F7FF\U00002702-\U000027B0]+")
count = 0
for ques in quesDF['question']:
    count += len(pattern.findall(ques))
print(count)

# q3
hole = " ".join(quesDF["question"]).lower().strip()
for c in ',.!?:;\()[]"}{':
    hole = hole.replace(c, '')
words = hole.split()
# print(*[f'{w}:{c}' for w,c in Counter(words).most_common(5)])  answer isn't accepted!
#  Answer isn't accepted!

print(-1)
print(-1)
