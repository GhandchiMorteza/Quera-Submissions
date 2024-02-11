n = int(input())

if n % 4 == 0:
    print(-n//4, n//4)
elif n % 4 == 1:
    print(-(n-1)//4, -(n-1)//4)
elif n % 4 == 2: 
    print((n+2)//4, -(n-2)//4)
else:
    print((n+1)//4, (n+1)//4)