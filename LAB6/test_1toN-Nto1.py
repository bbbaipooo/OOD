def oneToN(n):
    if n<=0:
        print(1,end=' ')
        return
    # if n==1:
    #     print(n,end=' ')
    else:
        oneToN(n-1)
        print(n,end=' ')
def nToOne(n):
    if n<=0:
        print(1,end=' ')
        return
    # if n==1:
    #     print(n,end=' ')
    else:
        print(n,end=' ')
        nToOne(n-1)
        
num=int(input('Enter Input : '))
oneToN(num)
nToOne(num)

def oneToN(n):
    if n<=0:
        print(1,end=' ')
        return
    else:
        oneToN(n-1)
        print(n,end=' ')
def nToOne(n):
    if n<=0:
        print(1,end=' ')
        return
    else:
        print(n,end=' ')
        nToOne(n-1)