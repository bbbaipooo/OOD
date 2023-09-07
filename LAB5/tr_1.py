def print1toN(n):
    if n<=0:
        print(1,end=' ')
    if n>1:
        print1toN(n-1)
        print(n,end=' ')
    elif n==1:
        print(n,end=' ')
    
def printNto1(n):
    if n<=0:
        print(1)
    if n>1:
        print(n,end=' ')
        printNto1(n-1)
    elif n==1:
        print(n,end=' ')
    
inp=input('Enter Input : ')
print1toN(int(inp))
printNto1(int(inp))