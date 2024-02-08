p, d = list(map(int, input().split()))
a = 1
while not 0 <= (a*d) % p <= p//2:
    a += 1
print(a*d)