def checkSort(l,i,n):
    if i==n:
        return 'Yes'
    else:
        if l[i]>l[i+1]:
            return 'No'
        return checkSort(l,i+1,n)


inp=list(map(int,input('Enter Input : ').split()))
print(checkSort(inp,0,len(inp)-1))
