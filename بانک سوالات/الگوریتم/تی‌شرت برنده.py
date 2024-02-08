a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*['no' if any(map(lambda x: x[0] < x[1], zip(a,b))) else 'yes'])