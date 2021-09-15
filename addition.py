no = str(input('Enter numbers to add: '))
count = 1
list = []
while count <= len(no):
    for item in no:
        list.append(int(item))
        count += 1
print(sum(list))
