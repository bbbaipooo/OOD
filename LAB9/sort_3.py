inp=list(map(int,input('Enter Input : ').split()))
c=True

for i in range(len(inp)):
    for j in range(i+1,len(inp)):
        if inp[i]>inp[j]:
            c=False

if c:print('Yes')
else:print('No')