strInput = input()

r = strInput.count('R')
y = strInput.count('Y')
g = strInput.count('G')

if r > 2 or (r > 1 and y > 1) or len(strInput) == y + r:
    print('nakhor lite')
else:
    print('rahat baash')