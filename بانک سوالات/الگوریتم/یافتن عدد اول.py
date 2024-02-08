n = int(input())
b = sum(list(map(int, str(n))))
count = 0

def isPrime(n):
    if n == 2:
        return True
    if n == 1 or not n % 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True 

while not count == b:
    n += 1
    if isPrime(n):
        count += 1
print(n)
