def forLoop(c,d):
    if d==c:
        return
    else:
        forLoop(c,d-1)
        print(f'FROM {a} TO {b} : i = {d-1}')

a,b=map(int,input('Enter Input : ').split())
forLoop(a,b)