tree = [[1]]
n = int(input())
for i in range(1, n):
    row = [1]
    prev_row = tree[i-1]
    row.extend([prev_row[i]+prev_row[i+1] for i in range(len(prev_row) - 1)])
    row.append(1)
    tree.append(row)

for el in tree:
    print(*el)