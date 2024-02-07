listB = list(map(int, input().split()))
listA = [1,1,2,2,2,8]

print(*[a - b for a, b in zip(listA, listB)])