a = input()
b = input()

print(f"{a} < {b}" if int(a[::-1]) < int(b[::-1]) else f"{a} = {b}" if a==b else f"{b} < {a}")