def Dream(weight_n,numBox,min):
    w_sumBox=0
    count=0
    for i in weight_n:
        if w_sumBox+i<=min:
            w_sumBox+=i
        else:
            count+=1
            w_sumBox=i
    if count+1==numBox:
        return min
    return Dream(weight_n,numBox,min+1)
    

weight_n,numBox=input('Enter Input : ').split('/')
weight_n,numBox=list(map(int,weight_n.split())),int(numBox)
print(f'Minimum weigth for {numBox} box(es) = {Dream(weight_n,numBox,max(weight_n))}')

