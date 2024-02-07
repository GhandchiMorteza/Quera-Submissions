arr = []

prod = 1
for i in range(4):
    n = int(input())
    prod *= n
    arr.append(n)
    
sumation = sum(arr)
average = sumation / 4
maxi = max(arr)
mini = min(arr)

print(f"Sum : {sumation:.6f}")
print(f"Average : {average:.6f}")
print(f"Product : {prod:.6f}")
print(f"MAX : {maxi:.6f}")
print(f"MIN : {mini:.6f}")
