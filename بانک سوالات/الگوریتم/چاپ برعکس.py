from collections import deque

arr = deque([])

while True:
    n = input()
    if n == '0':
        break
    arr.appendleft(n)

for item in arr:
    print(item)