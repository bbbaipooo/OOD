def appendAlp(inp):
    for i in inp:
        for j in i:
            if j>='a' and j<='z':
                alp.append(j)
    return alp
                
def isSort(lst,i,j,n):
    if j==n:return
    else:
        if lst[j]>lst[j+1]:lst[j],lst[j+1]=lst[j+1],lst[j]
        isSort(lst,i,j+1,n)
    if i==n:return
    else:return isSort(lst,i+1,j,n)

inp=input('Enter Input : ').split()
alp=[]
alp=appendAlp(inp)
isSort(alp,0,0,len(alp)-1)

while alp!=[]:
    for i in inp:
        for j in i:
            if alp!=[]:
                if j==alp[0]:
                    print(i,end=' ')
                    alp.pop(0)
                
                
            


            