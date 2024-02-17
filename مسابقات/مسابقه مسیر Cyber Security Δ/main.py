MOD = 10**9 + 7

e_name = input().strip()
r_len = int(input().strip())
max_v = 0
count = 0

for i in range(len(e_name) - r_len + 1):
    sub = e_name[i:i + r_len]
    val = sum([sub.count(c) for c in set(sub)])
    if val > max_v:
        max_v = val
        count = 1
    elif val == max_v:
        count += 1

print(count % MOD)
