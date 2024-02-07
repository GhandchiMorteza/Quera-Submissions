y, x = list(map(int, input().split()))
print(f'Right {11-y} {x}' if x < 11 else f'Left {11-y} {21-x}')