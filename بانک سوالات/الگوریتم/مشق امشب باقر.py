a, b, c = list(map(int, input().split()))

if a+b+c != 180:
    print('No')
elif not a or not b or not c:
    print('No')
else:
    print('Yes')