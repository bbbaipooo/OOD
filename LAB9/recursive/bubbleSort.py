def isSort(l,i,j,n):
    if j==n-1:return
    else:
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
        isSort(l,i,j+1,n)
    if i==n-1:return l
    else:return isSort(l,i+1,j,n)
    

s=[5,1,3,2,4] 

inp=list(map(int,input('Enter Input : ').split()))

print(isSort(inp,0,0,len(inp)-1))


def isSort(lst):
    for i in range(len(lst[:-1])): #num of all change
        for j in range(len(lst[:-1])): #swap
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
                
inp=list(map(int,input('Enter input : ').split()))

print(isSort(inp))