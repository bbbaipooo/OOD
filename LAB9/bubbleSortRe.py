def isSort1(lst):
    for i in range(len(lst[:-1])): #num of all change
        for j in range(len(lst[:-1])): #swap
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

def isSort(lst):
    pass

def Fgv(l, r, arr, x):
    if arr[l]>x[0]:
        print(arr[l])
    elif l<r:
        return Fgv(l+1,r,arr,x)
    elif l>=r:
        print("No First Greater Value")
    if len(x)!=1:
        return Fgv(l,r,arr,x[1:])



inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())),list(map(int, inp[1].split()))
Fgv(0, len(arr) - 1, sorted(arr), k)