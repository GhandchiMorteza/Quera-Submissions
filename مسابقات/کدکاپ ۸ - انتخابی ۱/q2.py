n, m = list(map(int, input().split()))

arr=[]
for i in range(n):
    row = ['A']
    if i == 0:
        row += ['A' for j in range(m-1)]
    elif i == (n-1):
        row += ['B' for j in range(m-1)]    
    else:
        row += ['.' for j in range(m-2)] + ['B']
    arr.append(row)
        
for row in arr:
    print(*row)