def GCD(m,n):
    if n==0:
        return m
    return GCD(abs(n),abs(m%n))
x,y=map(int,input('Enter Input : ').split())

if x>y:
    print(f'The gcd of {x} and {y} is : {GCD(x,y)}')
elif y>x:
    print(f'The gcd of {y} and {x} is : {GCD(y,x)}')
elif x==0 and y==0:
    print('Error! must be not all zero.')
