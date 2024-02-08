count = 0
n = int(input())
before = int(input())
for i in range(n-1):
    current = int(input())
    if current != before:
        count += 1
    before = current
print(count)