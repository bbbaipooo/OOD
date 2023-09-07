
lst=[5,4,2,1,3]
size=len(lst)


def insertionSort(lst):
    for i in range(size-1):
        last=lst[i+1]
        index=i+1
        for j in range(i+2):
            if last<lst[j] and j==0:
                lst.insert(j,lst.pop(index))
            if lst[j-1]<last and last<lst[j]:
                lst.insert(j,lst.pop(index))
            
insertionSort(lst)
print(lst)

# 4[1]3 2 
# --------
# 1 4|3 2
# 1 3 4|2 
# 1 2 3 4|