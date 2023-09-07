def isSort(lst):
    for i in range(len(lst)-1):
        move=lst[0]
        isMove=False
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                isMove=True
        if i+1==len(lst)-1:
            if isMove:
                print(f'last step : {lst} move[{move}]')
            else:
                print(f'last step : {lst} move[None]')
        elif isMove:
            print(f'{i+1} step : {lst} move[{move}]')

    
    
    
    
    
    
inp=list(map(int,input('Enter Input : ').split()))

isSort(inp)