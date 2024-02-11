_ = input()
arr = list(map(int, input().split()))

max_profit = 0
current_sum = 0
for n in arr:
    if current_sum + n <= 0:
        current_sum = 0
    else:
        current_sum += n
        if current_sum > max_profit:
            max_profit = current_sum

print(max_profit)