a = input()
o = input()
b = input()
if o == '*':
    print('1'+'0'*(len(a)+len(b)-2))
else:
    temp = [1]
    temp.extend([0]*(len(a)-1 if len(a) >= len(b) else len(b)-1))
    temp[-len(a) if len(a) < len(b) else -len(b)] += 1
    print("".join(map(str, temp)))