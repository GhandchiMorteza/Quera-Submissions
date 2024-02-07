summation = 0
count = 0
for i in range(1, int(input())+1):
    for j in range(1, int(i**0.5) + 1):
        if not i % j:
            count += 1
            summation += j
            if j != i // j:
                count += 1
                summation += i // j
print(count, summation)