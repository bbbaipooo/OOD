def isSort(lst):
    for i in range(len(lst)-1):
        maxV=lst[0]
        index=0
        for j in range(len(lst)-i):
            if lst[j]>maxV:
                maxV=lst[j]
                index=j
        lst[index],lst[len(lst)-i-1]=lst[len(lst)-i-1],lst[index]
    
    
l=[5,3,2,4,1]
isSort(l)
print(l)
# 3 2 4 1|5
# 3 2 1|4 5
# 2 1|3 4 5
# 1|2 3 4 5
