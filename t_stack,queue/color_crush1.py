class Stack():
    def __init__(self):
        self.lst=[]
    def pop(self):
        return self.lst.pop()
    def push(self,i):
        self.lst.append(i)
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return self.lst==[]
    def getStack(self):
        return 'Empty'if self.isEmpty() else self.lst

inp=input('Enter Input : ').split()
s=Stack()
combo=0

for i in inp:
    s.push(i)
    if s.size()>=3:
        b1=s.pop()
        b2=s.pop()
        b3=s.pop()
        if b1==b2==b3:
            combo+=1
        else:
            s.push(b3)
            s.push(b2)
            s.push(b1)


print(s.size())
print(*s.getStack(),sep='') #sepคือการทำให้เหมือนใน''
if combo>1:
    print('Combo :',combo,'! ! !')
#print('Empty','LOVE',sep='_')




