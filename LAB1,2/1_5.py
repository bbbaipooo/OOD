n=int(input('Enter Input : '))

for j in range(n+2):
    p=""
    for i in range(n-j+1):
        p+="."
    for i in range(j+1):
        p+="#"
    for i in range(n+2):
        if i==0 or j==0 or j==(n+1) or i==(n+1):
            p+="+"
        else:
            p+="#"
    print(p)
for j in range(n+2):
    p=""
    for i in range(n+2):
        if i==0 or j==0 or j==(n+1) or i==(n+1):
            p+="#"
        else:
            p+="+"
    for i in range(n-j+2):
        p+="+"
    for i in range(j):
        p+="."
    print(p)