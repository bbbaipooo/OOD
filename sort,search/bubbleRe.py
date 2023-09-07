def isSort(lst,i,j,n):
    if j==n:
        return
    else:
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
        isSort(lst,i,j+1,n)

    if i==n:
        return
    else:
        return isSort(lst,i+1,j,n)
    
    
l=[5,2,1,3,4]
inp=list(map(int,input('Enter Input : ').split()))
isSort(inp,0,0,len(inp)-1)
print(inp)
