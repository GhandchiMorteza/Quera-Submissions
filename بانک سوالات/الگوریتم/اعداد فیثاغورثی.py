i = input
a = int(i())
b = int(i())
c = int(i())

if a+b <= c or a+c <= b or b+c <= a:
    print('NO')
elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
    print('YES')
else:
    print('NO')