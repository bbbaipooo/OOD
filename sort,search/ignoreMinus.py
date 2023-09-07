def isSort(lst,i,j,n):
    if j==n:return
    else:
        if lst[j]>lst[j+1]:lst[j],lst[j+1]=lst[j+1],lst[j]
        isSort(lst,i,j+1,n)
    if i==n:return
    else:return isSort(lst,i+1,j,n)

inp=list(map(int,input('Enter Input : ').split()))
lpos=[]
for i in inp:
    if i>=0:
        lpos.append(i)
isSort(lpos,0,0,len(lpos)-1)
for i in inp:
    if i>=0:
        print(lpos.pop(0),end=' ')
    else:
        print(i,end=' ')

