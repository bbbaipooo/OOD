def checkSort(val):
    l=val[1:]
    for i in range(len(val)-1):
        if val[i]>l[i]:
            return 'No'
    return 'Yes'

inp=list(map(int,input('Enter Input : ').split()))
print(checkSort(inp))