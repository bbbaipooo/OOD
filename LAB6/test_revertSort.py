def findMax(itm):
    if len(itm)==1:
        return itm[0]
    MAX=findMax(itm[1:])
    return MAX if MAX>itm[0] else itm[0]


def revertSort(itm,temp=[]):
    if len(itm)==0:
        return temp
    else:
        m=findMax(itm)
        temp.append(m)
        itm.remove(m)
        return revertSort(itm,temp)



item=list(map(int,input('Enter Input : ').split()))
print(revertSort(item))