a = int(input())
b = int(input())

def is_prime(n):
    if not n % 2:
        return False
    for i in range(3, n//2, 2):
        if not n % i:
            return False
    return True

for i in range(a, b+1):
    if i == 1:
        continue
    if i == 2:
        print(2)
        continue
    if is_prime(i):
        print(i)
    if not i % 2:
        i += 1