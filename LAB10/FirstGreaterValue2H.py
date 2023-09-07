def Fgv(l, r, arr, x):
    if arr[l]>x[0]:
        print(arr[l])
    elif l>=r:
        print("No First Greater Value")
    elif l<r:
        return Fgv(l+1,r,arr,x) #move left
    
    if len(x)!=1:
        return Fgv(l,r,arr,x[1:]) #move right



inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())),list(map(int, inp[1].split()))
Fgv(0, len(arr) - 1, sorted(arr), k)