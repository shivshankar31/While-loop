# least common factor or multiple

no1 = int(input('Enter first number: '))
no2 = int(input('Enter second number: '))

big = no1 if no1 > no2 else no2
while True:
    if big % no1 == 0 and big % no2 == 0:
        print("LCM ", big)
        break
    big += 1
