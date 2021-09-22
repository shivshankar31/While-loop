# decimal to binary

print('Decimal to Binary Converter')
no=int(input("Enter Decimal Number: "))
rem = ''
while no>0:
    rem= str(no%2)+ rem
    no=no//2
else:
    print('Binary value is :',rem)
