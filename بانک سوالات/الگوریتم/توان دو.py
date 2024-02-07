import math

n = int(input())
log2n = math.log2(n)
print(2**math.ceil(log2n) if log2n != math.ceil(log2n) else 2*n )