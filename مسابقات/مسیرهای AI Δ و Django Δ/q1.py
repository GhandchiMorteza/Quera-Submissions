n = int(input())
matrix = [['.' for _ in range(2 * n - 1)] for _ in range(n)]
for i in range(n):
    if i < n - 1:  
        matrix[i][n - i - 1] = 'D'  
        matrix[i][n + i - 1] = 'D' 
    else:  
        for j in range(2 * n - 1):
            if j % 2 == 0:
                matrix[i][j] = 'D'
            else:
                matrix[i][j] = '.'       
print('\n'.join(''.join(row) for row in matrix))
