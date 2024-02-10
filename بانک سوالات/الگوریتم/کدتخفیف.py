n, t = list(input().split())
pattern = set(t)

for _ in range(int(n)):
    print('Yes' if pattern == set(input()) else 'No')