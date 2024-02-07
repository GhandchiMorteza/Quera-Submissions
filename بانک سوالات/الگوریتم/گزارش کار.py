n, k = list(map(int, input().split()))
for i in range(n):
    k -= int(input())
    if k <= 0:
        break
    
print(*['YES' if k <= 0 else 'NO'])