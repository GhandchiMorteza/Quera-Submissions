k = int(input())
s = ''
for i in range(1, 5000):
    s += str(i)
    if len(s) >= k:
        print(s[k-1])
        break