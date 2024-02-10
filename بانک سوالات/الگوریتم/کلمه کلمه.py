count = 0
n = input()
for c in 'aeiuo':
    count += n.count(c)
print(2**count)