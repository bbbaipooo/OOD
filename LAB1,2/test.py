num=int(input('Enter height: '))
for i in range((num-1)*2):
    print('A',end='')
print('1')
for i in range(num-1):
    for k in range(num-i+1):
        print('A',end='')
    for j in range(1):
        print('1')
    print()

