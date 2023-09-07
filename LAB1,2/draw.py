from tkinter import N


n=int(input('number : '))

for y in range(n):
    for x in range(n):
        print('(',x,',',y,'),',sep='',end='') #(1,1)
    print()