def checkSort(val):
    b=val[:-1]
    for i in range(len(b)):
        if b[i]>val[i+1]:
            return 'No'
    return 'Yes'

inp=list(map(int,input('Enter Input : ').split()))
print(checkSort(inp))