def isSort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                return 'no'
    return "yes"

def isSortRe(lst,i,j,n):
    if j==n:return
    else:
        if lst[j]>lst[j+1]:return 'No'
        isSortRe(lst,i,j+1,n)
    if i==n:return 'Yes'
    else:return isSortRe(lst,i+1,j,n)
        

inp=list(map(int,input('Enter Input : ').split()))
print(isSort(inp))
print(isSortRe(inp,0,0,len(inp)-1))