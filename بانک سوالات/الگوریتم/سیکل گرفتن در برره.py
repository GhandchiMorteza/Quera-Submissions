from math import ceil


n = int(input())
answers = input()

patterns = {
        'keyvoon': [3,3,1,1,2,2], 
        'nezam': [1,2,3],           
        'shir farhad': [2,1,2,3],  
    }

scores = {name: 0 for name in patterns.keys()}

for i, answer in enumerate(answers):
    key = int(answer)
    for name, pattern in patterns.items():
        if key == pattern[i % len(pattern)]:
            scores[name] += 1    

highest_score = max(scores.values())
print(highest_score)
for name,score in scores.items():
    if score == highest_score:
        print(name)