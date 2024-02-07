n, k = list(map(int, input().split()))
count = 0
for i in range(n):
    count += input().count('*')
print(count)