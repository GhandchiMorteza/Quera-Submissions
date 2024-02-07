import math

a,b,l = list(map(int, input().split()))

# a wait ! b wait ! a wait ! b wait
print(math.ceil(l/2) * a + math.floor(l/2) * b)