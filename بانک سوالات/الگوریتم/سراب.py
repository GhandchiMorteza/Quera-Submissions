for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    if not (x == y or x-2 == y):
        print(-1)
    elif x == y:
        print(*[2*x-1 if x%2 else 2*x])
    else:
        x -= 1
        y += 1
        print(*[2*x if x%2 else 2*x-1])