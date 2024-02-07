max = 0
for _ in range(int(input())):
    distinctCount = len(set(input()))
    if distinctCount > max:
        max = distinctCount
print(max)