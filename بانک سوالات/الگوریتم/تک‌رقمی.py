n = input()

while len(n) > 1:
    n = str(sum(list(map(int, n))))

print(n)