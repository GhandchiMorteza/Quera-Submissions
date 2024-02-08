h, m = list(map(int, input().split()))
print(f"{(12-h)%12:02d}:{(60-m)%60:02d}")