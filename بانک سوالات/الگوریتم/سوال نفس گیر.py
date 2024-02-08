_ = input()
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
print(sum(map(lambda t: t[0] * t[1], zip(listA, listB))))