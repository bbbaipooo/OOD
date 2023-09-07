a=[1,2,3,4]
b=['4','5','6','7']

print(*a)
print(*b,sep=',')

inp = [int(i) for i in input('Enter Input : ').split()]