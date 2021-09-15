
# divisor Program

no1 = int(input('Enter a number: '))
div = int(input('Enter divisor number:'))
count = 0
while div < no1:
    if no1 % div == 0:
        print(div)
        count += 1
    div += 1

print("No. of divisors are ", count)
if count == 0:
    print("Prime Number ")
else:
    print("Not Prime Number")
