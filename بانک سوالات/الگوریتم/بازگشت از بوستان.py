x, _ = list(map(int, input().split()))
x1, _ = list(map(int, input().split()))
print(*['Right' if x1 > x else 'Left'])