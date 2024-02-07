n = int(input())
simDiv = 1

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        simDiv += i
        if i != n // i:
            simDiv += n // i

print('YES' if n == simDiv else 'NO')