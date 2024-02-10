def gcdRecursive(a, b):
    if not b:
        return a
    return gcdRecursive(b, a%b)

def lcm(gcd, product):
    return product // gcd

n, m = list(map(int, input().split()))
if n > m:
    n, m = n, m
gcd = gcdRecursive(m, n)
lcmVal = lcm(gcd, m*n)

print(gcd, lcmVal)