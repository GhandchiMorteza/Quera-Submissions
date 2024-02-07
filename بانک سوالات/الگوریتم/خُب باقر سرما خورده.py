arr = []

for i in range(5):
    line = input()
    if line.find('MOLANA') != -1 or line.find('HAFEZ') != -1:
        arr.append(i+1)

print(*arr if len(arr) else 'NOT FOUND!')
