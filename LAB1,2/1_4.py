print('*** Fun with Drawing ***')
x = int(input('Enter input : '))
for k in range(x*2-1):
    for j in range(x*2-1):
        if(k>=j):
            if(j%2==0):
                print('#',end='')
            elif(j%2==1):
                print('.',end='')
        elif(k<j):
            if(k%2==0):
                print('#',end='')
            elif(k%2==1):
                print('.',end='')  
        if(k<j):
            if(k%2==0):
                print('#',end='')
            elif(k%2==1):
                print('.',end='')

    for j in range(x*2-2):
        if(k-1>=j):
            if((k%2==1 and j%2==1)or(k%2==0 and j%2==0)):
                print('.',end='')
            else:
                print('#',end='')
    print()
for k in range(x*2-3):
    for j in range(x*2-1):
        if(j>k):
            if((k%2==1 and j%2==1)or(k%2==0 and j%2==0)):
                print('.',end='')
            else:
                print('#',end='')
    for j in range(x*2-2):
        if(k>=j):
            if(k%2==0):
                print('.',end='')
            else:
                print('#',end='')
        if(k>=j):
            if(k%2==0):
                print('.',end='')
            else:
                print('#',end='')
    for j in range(x*2-1):
        if(j-1>k):
            if((j%2==1)):
                print('.',end='')
            else:
                print('#',end='')
    print()
for k in range(x*4-3):
    print('#',end='')