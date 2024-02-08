from decimal import Decimal
n = int(input())
m = int(input())

print(sum(sum((Decimal(i)+Decimal(j))**3//Decimal(j)**2 for j in range(1, n+1)) for i in range(-10, m+1)))
