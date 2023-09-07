# l=[4,5,3,2,1]



inp=list(map(int,input('Enter Input : ').split()))
for i in range(len(inp)-1):
    for j in range(len(inp)-1):
        if inp[j]>inp[j+1]:
            val=inp[j]
            inp[j],inp[j+1]=inp[j+1],inp[j]
            print(inp[j],'mmm')
    print(f"#{i+1} step : {inp} move[{inp[j]}]")
    val=inp[0]
# print(inp)



# Enter Input : 4 3 2 1
# 1 step : [3, 2, 1, 4] move[4]
# 2 step : [2, 1, 3, 4] move[3]
# last step : [1, 2, 3, 4] move[2]