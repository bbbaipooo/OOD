def power(n,p):
    if p==0:
        return 1
    return n*power(n,p-1)

n,p=input('Enter Input a b : ').split()
print(power(int(n),int(p)))