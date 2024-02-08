m, s = list(map(int, input().split()))

if s == m:
    print('Saal Noo Mobarak!')
else:
    print(*['L'*(m-s) if s < m else 'R'*(-m+s)])