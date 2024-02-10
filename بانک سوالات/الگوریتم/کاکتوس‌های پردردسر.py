_ = input()
for n in list(map(int, input().split())):
    if n <= 3:
        print('*' * n)
    else:
        print('*')