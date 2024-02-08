from math import ceil
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(n-ceil(sum(arr)/k))