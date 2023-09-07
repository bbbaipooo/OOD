def print1ToN(n):
    if n<=0:
        print(1,end=' ')
    else:
        if n==1:
            print(n,end=' ')
        else:
            print1ToN(n-1)
            print(n,end=' ')

def printNTo1(n):
    if n<=0:
        print(1,end=' ')
    else:
        if n>1:
            print(n,end=' ')
            return printNTo1(n-1)
        elif n==1:
            print(n)
    
n=int(input('Enter Input : '))
print1ToN(n)
printNTo1(n)