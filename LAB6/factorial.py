def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)

inp=int(input('Enter Input : '))
print(fac(inp))