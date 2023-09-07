def starCase(n,i):
    if n>0:
        if n==0:
            return
        else:
            print('_'*(n-1)+'#'*i)
            starCase(n-1,i+1)
    elif n<0:
        if -n==0:
            return
        else:
            print('_'*(i-1)+'#'*(-n))
            starCase(n+1,i+1)
    elif n==0 and i==1:
        print('Not Draw!')

starCase(int(input('Enter Input : ')),1)