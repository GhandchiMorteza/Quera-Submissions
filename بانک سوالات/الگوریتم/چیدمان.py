arr = []
for _ in range(int(input())):
    arr.append(int(input()))
should = sum(arr)//len(arr)
diff = 0
for el in arr:
    diff += (el - should) if el > should else (should - el)
print(diff // 2)