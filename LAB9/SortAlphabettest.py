l=[6,9,8,5,4,11,10,12]
# 68549
# 65489
# 54689
# 45689
c=len(l)-1
while c:
    c-=1
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
    
print(l)
        