xPos = []
yPos = []

for _ in range(3):
    x, y = list(map(int, input().split()))
    xPos.append(x)
    yPos.append(y)

print(*[i for i in xPos if xPos.count(i) == 1 ], *[i for i in yPos if yPos.count(i) == 1 ])