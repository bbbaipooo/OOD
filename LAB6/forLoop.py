def forLoop(s,e):
    if s==e:
        #print(f'FROM {s} TO {b} : i = {e}')
        return 1
    forLoop(s,e-1)
    print(f'FROM {s} TO {b} : i = {e-1}')

a,b=map(int,input('Enter Input : ').split())
forLoop(a,b)