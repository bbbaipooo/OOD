def printSum(n):
    if n==1:
        print(n,end='')
    else: 
        printSum(n-1)
        print(f' + {n}',end='')
        
def sortSum(n):
    if n==1:
        return 1
    return n+sortSum(n-1)

s=int(input('Enter Input : '))
printSum(s)
print(f' = {sortSum(s)}')

