def drawT(n,i):
    if n>0:
        if n==0:
            return
        else:
            print('^'*(n-1)+'#'*((i*2)-1)+'^'*(n-1))
            drawT(n-1,i+1)
    elif n<=0 and i==1:
        print('Not Draw!')
        

drawT(int(input('Enter input : ')),1)