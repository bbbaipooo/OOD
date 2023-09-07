
m=[1,2,3,4,5]
for u in m:
    print(u,end='')
print()
for u in m[::]:
    print(u,end='')
print()
for u in m[::-1]:
    print(u,end='')
print()
for u in m[1::-1]:
    print(u,end='')
    
    
t=[str('A') for i in range(5)]
print(t)