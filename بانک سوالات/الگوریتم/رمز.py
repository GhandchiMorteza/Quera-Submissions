_ = int(input())
s = input()
sum = 0
for c in s:
    code = input()
    chap = code.index(c)
    rast = 9 - chap
    sum += chap if chap <= rast else rast
print(sum)