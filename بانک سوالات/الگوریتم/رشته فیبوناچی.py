i = 1
s = 1
output = ''
for j in range(1, int(input()) + 1):
        if j == s:
            output += '+'
            s, i = i+s, s
        else:
            output += '-'
              
print(output)    