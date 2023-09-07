def GCD(m,n):
    if n==0:
        return m
    return GCD(abs(n),abs(m%n))
        

x,y=map(int,input('Enter Input : ').split())
if x>y:
    print(GCD(x,y))
elif y>x:
    print(GCD(y,x))
elif y==0 and x==0:
    print('input = 0')
