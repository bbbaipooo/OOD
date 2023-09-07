def isSort(lst):
    for i in range(len(lst[:-1])):
        for j in range(len(lst[:-1])):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
                
inp=list(map(int,input('Enter Input : ').split()))
pos=[]
for i in inp:
    if i>=0:
        pos.append(i)
        
pos=isSort(pos)

for i in inp:
    if i>=0:
        print(pos.pop(0),end=' ')
    else:
        print(i,end=' ')
        