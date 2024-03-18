x ={}
y = {}
z = {}
for _ in range(7):
    a,b,c = list(map(int, input().split()))
    if a not in x:
        x[a] = 1
    else:
        x[a] += 1
    if b not in y:
        y[b] = 1
    else:
        y[b] += 1
    if c not in z:
        z[c] = 1
    else:
        z[c] += 1
output = []     
for key, value in x.items():
    if value == 3:
        output.append(key)
for key, value in y.items():
    if value == 3:
        output.append(key)
for key, value in z.items():
    if value == 3:
        output.append(key) 
print(*output)