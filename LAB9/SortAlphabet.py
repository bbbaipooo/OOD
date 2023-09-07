def findAlphabet(inp):
    for lst in inp:
        for i in lst:
            if i>='a' and i<='z':
                alp.append(i)

def isSort(val):
    num=len(val)-1
    while num:
        num-=1
        for i in range(len(val)-1):
            if val[i]>val[i+1]:
                val[i],val[i+1]=val[i+1],val[i]
    return val
        
    
inp=input('Enter Input : ').split()
alp=[]
findAlphabet(inp)
alpSort=isSort(alp)

while alpSort!=[]:
    for lst in inp:
        for i in lst:
            if alpSort:    
                if i==alpSort[0]:
                    print(lst,end=' ')
                    alpSort.pop(0)
                