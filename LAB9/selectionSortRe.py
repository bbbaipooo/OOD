# size=len(l)

# for i in range(size-1):
#    maxV=l[0]
#    index=0
#    for j in range(size-i):
#       if l[j]>maxV:
#          maxV=l[j]
#          index=j
#          #print(maxV,index)
#    l[index],l[size-i-1]=l[size-i-1],l[index] 

l=[6,9,8,5,4]
size=len(l)

def selectSort(lst,i,j,maxV,index):
    if j>size-i-1:
        return
    else:
        lst[j]>maxV
        maxV=l[j]
        index=j
        selectSort(lst,i,j+1,maxV,index)
        
    if i>=size-2:
        return 
    else:
        l[index],l[size-i-1]=l[size-i-1],l[index] 
        maxV=lst[0]
        index=0
        return selectSort(lst,i+1,j,maxV,index)
    
selectSort(l,0,0,l[0],0)
print(l)

        


    
