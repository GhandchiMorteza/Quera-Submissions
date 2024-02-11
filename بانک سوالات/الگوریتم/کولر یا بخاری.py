n = int(input())
for element in list(map(int, input().split())):
    if element > 15:
        print('cooler')
    else:
        print('heater')