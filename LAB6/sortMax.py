# def isMax(l):
#     return
def isMax(lst):
    if len(lst)==1:
        return lst[0]
    else:
        mx = isMax(lst[1:])
        print(mx)
        return mx if mx>lst[0] else lst[0]
         
    
    
inp=list(map(int,input('Enter i8nput : ').split()))
