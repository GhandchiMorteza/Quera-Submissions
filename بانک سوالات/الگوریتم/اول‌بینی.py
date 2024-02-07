a = int(input())
b = int(input())

def is_prime(n: int) -> bool:
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, n//2+1):
        if not n % i:
            return False
    return True

primes_list = []
for i in range(a+1, b):
    if is_prime(i):
        primes_list.append(i)
print(','.join(map(str, primes_list)))