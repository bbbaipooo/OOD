def isSort(inp):
    for i in range(len(inp)-1):
        for j in range(len(inp[:-1])):
            if inp[j][1]<inp[j+1][1]:
                inp[j],inp[j+1]=inp[j+1],inp[j]
            elif inp[j][1]==inp[j+1][1]:
                if inp[j][2]<inp[j+1][2]:
                    inp[j],inp[j+1]=inp[j+1],inp[j]
        
    
inp=input('Enter Input : ').split('/')

#print(inp)
#['Manchester United,30,3,5,88,20', 'Arsenal,24,6,8,98,29', 'Chelsea,22,8,8,98,29']

for i in range(len(inp)):
    inp[i]=inp[i].split(',')
    inp[i]=[inp[i][0] , (int(inp[i][1])*3)+int(inp[i][3]) , int(inp[i][4])-int(inp[i][5])]

#print(inp) 
#[['Manchester United', 95, 68], ['Arsenal', 80, 69], ['Chelsea', 74, 69]]

print("== results ==")

isSort(inp)
for i in range(len(inp)):
    print(f'[\'{inp[i][0]}\', ','{\'points\': ',inp[i][1],'}, {\'gd\': ',f'{inp[i][2]}','}]',sep='')
# "== results ==
# ['Manchester City', {'points': 92}, {'gd': 82}]
# ['Arsenal', {'points': 92}, {'gd': 48}]
# ['Liverpool', {'points': 80}, {'gd': 89}]"
    



# for i in inp:
#     i=i.split(',')
#     print(i)
#     i=[i[0] , (int(i[1])*3)+int(i[3]) , int(i[4])-int(i[5])]

    

    
