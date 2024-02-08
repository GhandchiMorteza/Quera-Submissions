n, k = list(map(int, input().split()))

for a in range(n):
        if (a * k + k) % n == 0:
            print(a+1)
            break