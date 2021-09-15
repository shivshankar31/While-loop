# Find Greatest Common Divisor

no1 = int(input('Enter first number: '))
no2 = int(input('Enter second number: '))
div = int(input('Enter divisor: '))
print(' ')
count = 0
small = no1 if no1 < no2 else no2
last = -1
while div < no2:
    if no1 % div == 0 and no2 % div == 0:
        last = div
        count += 1
    div += 1
else:
    if last < 0:
        print("No Common Divisor found")
    else:
        print("Greatest Common Divisor ", last)
