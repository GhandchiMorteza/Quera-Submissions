a, b, c = list(map(int, input().split()))
matrix = []
for _ in range(3):
    s, e = list(map(int, input().split()))
    matrix.append([i for i in range(s, e)])

a3 = [value for value in matrix[0] if value in matrix[1] and value in matrix[2]]
a2 = [value for value in matrix[0] if value not in a3 and (value in matrix[1] or value in matrix[2])] + [value for value in matrix[1] if value not in matrix[0] and value in matrix[2]]
a1 = [value for value in matrix[0]+matrix[1]+matrix[2] if value not in a2+a3]
print(len(a1)*a*1 + len(a2)*b*2 + len(a3)*c*3)