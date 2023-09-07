def sortPower(a,b):
    if b==0:
        return 1
    else:
        return a*sortPower(a,b-1)


a,b=map(int,input('Enter Input a b : ').split())
print(sortPower(a,b))