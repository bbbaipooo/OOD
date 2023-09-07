def isSort(lst):
    for i in range(len(lst[:-1])): #num of all change
        for j in range(len(lst[:-1])): #swap
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
                
inp=list(map(int,input('Enter input : ').split()))

print(isSort(inp))