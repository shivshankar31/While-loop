print('To find common divisor between two numbers')
no1 = int(input('Enter first number: '))
no2 = int(input('Enter second number: '))
div = int(input('Enter divisor: '))
print(' ')
count = 0
small = no1 if no1 < no2 else no2
while div < no2:
    if no1 % div == 0 and no2 % div == 0:
        print('Common divisors are:')
        print(div)
        print(' ')
        count += 1
    div += 1

print('Total common divisors are:', count)
if count == 0:
    print('Its a prime number')
else:
    print('Its not a prime number ')
