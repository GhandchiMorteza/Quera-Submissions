n = int(input())
m = float(input())

bmi = n / m ** 2
halat = ''
if bmi < 18.5:
    halat = 'Underweight'
elif 18.5 <= bmi < 25:
    halat = 'Normal'
elif 25 <= bmi < 30:
    halat = 'Overweight'
elif 30 <= bmi:
    halat = 'Obese'

print("%.2f" % bmi)
print(halat)