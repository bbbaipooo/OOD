def isSort(inp):
    for i in range(len(inp)-1):
        for j in range(len(inp)-1):
            if inp[j][1]<inp[j+1][1]:
                inp[j],inp[j+1]=inp[j+1],inp[j]
            elif inp[j][1]==inp[j+1][1]:
                if inp[j][2]<inp[j+1][2]:
                    inp[j],inp[j+1]=inp[j+1],inp[j]

# Manchester United,30,3,5,88,20/Arsenal,24,6,8,98,29/Chelsea,22,8,8,98,29
#['Manchester United,30,3,5,88,20', 'Arsenal,24,6,8,98,29', 'Chelsea,22,8,8,98,29']
inp=input('Enter Input : ').split('/')

for i in range(len(inp)):
    inp[i]=inp[i].split(',')
    inp[i]=[inp[i][0],(int(inp[i][1])*3)+int(inp[i][3]),int(inp[i][4])-int(inp[i][5])]
    
print('== results ==')
isSort(inp)
for i in range(len(inp)):
    print('[\'%s\', {\'points\': %d}, {\'gd\': %d}]'%(inp[i][0], inp[i][1], inp[i][2]))

#['Manchester United', {'points': 95}, {'gd': 68}]

    
