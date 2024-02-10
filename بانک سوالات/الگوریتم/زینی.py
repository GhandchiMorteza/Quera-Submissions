n, m = list(map(int, input().split()))

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

count = 0
for i, row in enumerate(matrix):
    if i == n-1 or i == 0:
        continue
    for j, value in enumerate(row):
        if j == m-1 or j == 0:
            continue
        if row[j-1] < value and row[j+1] < value and matrix[i-1][j] > value and matrix[i+1][j] > value:
            count += 1
        elif row[j-1] > value and row[j+1] > value and matrix[i-1][j] < value and matrix[i+1][j] < value:
            count += 1
        
print(count)