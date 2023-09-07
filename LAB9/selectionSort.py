l=[6,9,8,5,4]
size=len(l)

for i in range(size-1):
   maxV=l[0]
   index=0
   for j in range(size-i):
      if l[j]>maxV:
         maxV=l[j]
         index=j
         #print(maxV,index)
   l[index],l[size-i-1]=l[size-i-1],l[index] 
print(l)


# def selectSort(l):return [l.pop(l.index(min(l))) for i in l.copy()]
    
# l=[6,9,8,5,4]
# print(selectSort(l))


#--ref line 7--
# 6 4 8 5 9|
# 6 4 8 5|9 
# 6 4 5|8 9
# 5 4|6 8 9
# 4|5 6 8 9
   