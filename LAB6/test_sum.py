def resultSum(n):
    if n==0:
        return 0
    else:
        return n+resultSum(n-1)
def printSum(n):
    if n==1:
        print(n,end='')
    else:
        printSum(n-1)
        print(f' + {n}',end='')


num=int(input('Ebter Input : '))
printSum(num)
print(f' = {resultSum(num)}')