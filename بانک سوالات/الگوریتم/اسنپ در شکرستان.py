n, t = list(map(int, input().split()))
matrix = []

for _ in range(n):
    row = list((map(int, input().split())))
    matrix.append(row)

sum = 0
for _ in range(t):
    i, j = list(map(int, input().split()))
    sum += matrix[i-1][j-1]
    
print(sum)