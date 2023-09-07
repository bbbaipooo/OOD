def sortMax(ll):
    if len(ll)==1:
        return ll[0]
    MAX=sortMax(ll[1:])
    return MAX if MAX>ll[0] else ll[0]


def revertSort(ll,temp=[]):
    if len(ll)==0:
        return temp
    else:
        maxS=sortMax(ll)
        temp.append(maxS)
        ll.remove(maxS)
        return revertSort(ll,temp)

item=list(map(int,input('Enter your List : ').split(',')))
print(f'List after sorted : {revertSort(item)}')
