class Stack:
    # class Stack
    def __init__(self,list=None):
        if list==None:
            self.items=[]
        else:
            self.items=list

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items==[]
    
    def size(self):
        return len(self.items)


t_input=input('Enter Input : ').split(',')
s=Stack()

for i in t_input:    
    if i[0]=='A':
        char,num = i.split()   # num = i.replace('A ','') <-ใช้วิธีนี้ไม่ต้องsplitหลายรอบ
        s.push(num)
        print('Add =',s.peek(),'and Size =',s.size())
    elif i[0]=='P':
        if s.size()>0:
            print('Pop =',s.pop(),'and Index =',s.size())
        elif s.isEmpty():
            print('-1')

if(s.size() == 0):
    print("Value in Stack = Empty")
else:
    i = int(0)
    j = s.size()
    y = []
    while i < j:
        y.append(s.pop())
        i = i + 1
    print("Value in Stack =",end='')
    while j > 0:
        j -= 1
        print("",y[j],end='')



