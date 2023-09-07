def isSort(lst):
    for i in range(len(lst)-1):
        cl=lst[i+1]
        index=i+1
        for j in range(i+2):
            if lst[i+1]<lst[j]:
                lst[i+1],lst[j]=lst[j],lst[i+1]
    return lst

l=[5,3,2,4,1]
# 3 5|2 4 1
# 2 3 5|1 4
# 1 2 3 5|4
# 1 2 3 4 5|

print(isSort(l))