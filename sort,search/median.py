def isSort(lst,i,n):
    if i==n:
        return
    else:
        print(f'list = {lst[:i+1]} : median = {median(lst[:i+1])}')
        return isSort(lst,i+1,n)
    
def median(lt):
    if len(lt)%2==1:
        return float(lt[len(lt)//2])
    else:
        return (lt[len(lt)//2]+lt[(len(lt)//2)-1])/2

l = [e for e in input("Enter Input : ").split()]
l=list(map(int, l))
isSort(l,0,len(l)-1)