def khord(target, x, y):
    for i in range(target//x+1):
        if (target - x * i) % y == 0: 
            return([i, (target - x*i)//y])
    return [-1]


target, x, y = list(map(int, input().split()))
print(*khord(target, x, y))