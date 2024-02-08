n = int(input())
print("1")
before_arr = [1]
for i in range(n-1):
    curr_arr = [1]
    for j in range(i):
        curr_arr.append(before_arr[j] + before_arr[j+1])
    curr_arr.append(1)
    print(*curr_arr)
    before_arr = curr_arr