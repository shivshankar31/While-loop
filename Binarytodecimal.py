# binary to decimal
from math import pow
no = 1111
deci = 0
i = 0
while no>0:
    rem=no%10
    val = rem * int(pow(2,i))
    deci = deci+val
    no = no//10
    i+=1

else:
    print(deci)
