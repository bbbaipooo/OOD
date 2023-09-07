def fibo(n):
    if n==0:
        return False
    if n==1:
        return 0
    elif n==2 or n==3:
        return 1
    return fibo(n-1)+fibo(n-2)
    

inp=int(input('Enter Input : '))
if fibo(inp):
    print(fibo(inp))
else:print('Error')








# 0 1 1 2 3 5 8 13 21