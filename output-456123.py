Output – 456123

no = 123456 # output 456123
rev = 0
while no > 0:
    rev = (rev * 1000) + no % 1000
    no = no//1000
else:
    print(rev)
