list_shoc = list(map(int, input().split()))
list_khordan = [0, 0, 0, 0]
i = -1
while not list_shoc.count(0):
    i += 1
    i %= 4
    list_shoc[i] -= 1
    list_khordan[i] += 1
    list_shoc.append(list_shoc[0])
    list_shoc.pop(0)
    
print(*list_khordan)