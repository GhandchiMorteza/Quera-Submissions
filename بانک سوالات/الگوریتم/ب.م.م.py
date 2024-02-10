a = int(input())
b = int(input())


def gcdRecursive(a, b):
    if not b:
        return a
    return gcdRecursive(b, a % b)

if a < b:
    a, b = b, a
print(gcdRecursive(a, b))