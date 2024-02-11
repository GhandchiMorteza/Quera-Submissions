dic = {}
for _ in range(int(input())):
    name = list(input().split())[0]
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1

print(max(dic.values()))