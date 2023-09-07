

inp=input('Enter Input : ').split('/')
lft,rht=list(map(int,inp[0].split())),list(map(int,inp[1].split()))
lft=sorted(lft)

for i in rht:
    c=False
    for j in lft:
        if c==False:
            if lft[-1]<i:
                print("No First Greater Value")
                c=True
            elif j>i:
                print(j)
                c=True
            

