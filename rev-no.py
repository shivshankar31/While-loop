# print reverse output 654321


no = 123456
rev = 0
while no>0:
    rev = (rev * 10) + no%10
    no = no//10
else:
    print(rev)
