def can_seat_group(s, l):
    consecutive_zeros = 0
    for i in range(s-1, n):
        if computers[i] == 0:
            consecutive_zeros += 1
            if consecutive_zeros == l:
                return True, i - l + 1
        else:
            consecutive_zeros = 0  
    return False, -1

def fill_ones_for_consecutive_zeros(start_index, l):
    for j in range(start_index, start_index + l):
        computers[j] = 1

n, m = list(map(int, input().split()))
computers = [0] * n
for _ in range(m):
    s, l = list(map(int, input().split()))
    can_seat, start_index = can_seat_group(s, l)
    if can_seat:
        fill_ones_for_consecutive_zeros(start_index, l)
    print(''.join(str(i) for i in computers))
