class Stack():
    def __init__(self):
        self.lst=[]
    def pop(self):
        return self.lst.pop()
    def push(self,i):
        self.lst.append(i)
    def peek(self):
        return self.lst[-1]
    def isEmpty(self):
        return self.lst==[]
    def size(self):
        return len(self.lst)
    def getStack(self):
        return self.lst

dec=int(input('Enter Decimal : '))
b=Stack()

while dec>0:
    if dec%2==1:
        b.push(1)
        dec=dec//2
    else:
        b.push(0)
        dec=dec//2

print('Binary : ',end='')
while not b.isEmpty():
    print(b.pop(),end='')

