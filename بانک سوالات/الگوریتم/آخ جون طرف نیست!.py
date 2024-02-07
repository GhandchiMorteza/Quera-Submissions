_ = input()
a = set(input().split())

_ = input()
b = set(input().split())

_ = input()
c = set(input().split())

print(7 - len(a.union(b, c)))