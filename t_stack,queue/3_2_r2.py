class Stack():
    def __init__(self):
        self.lst = []

    def pop(self):
        return self.lst.pop()

    def push(self, i):
        self.lst.append(i)

    def peek(self):
        return self.lst[-1]

    def isEmpty(self):
        return self.lst == []

    def size(self):
        return len(self.lst)


def ManageStack(inp):
    
    for i in inp:
        order = i.split()
        if order[0] == 'A':
            s.push(int(order[1]))
            print('Add =', order[1])
        elif order[0] == 'P':
            if s.isEmpty():
                print(-1)
            else:
                print('Pop = ',s.pop())
        elif order[0] == 'D': 
            if s.isEmpty():
                print(-1)
            else:       
                while not s.isEmpty():
                    if int(order[1])==int(s.peek()):
                        print('Delete =', s.pop())
                    else:
                        k.push(s.pop())
                while not k.isEmpty():
                    s.push(k.pop())
        elif order[0]=='LD':   
            if s.isEmpty():
                print(-1)
            else:       
                while not s.isEmpty():
                    if int(order[1])>int(s.peek()):    # *****************ระวัง!!!!!!! ค่าที่เรารับเข้ามามันเป็นstrแล้วเราเอามาเทียบแบบเลขจำนวนเต็มได้ยังไง***********************
                        print('Delete =', s.peek(), 'Because',s.pop(), 'is less than', order[1])
                    else:
                        k.push(s.pop())
                while not k.isEmpty():
                    s.push(k.pop())
        elif order[0]=='MD':      
            if s.isEmpty():
                print(-1)
            else:  
                while not s.isEmpty():
                    if int(order[1])<int(s.peek()):    # ****************************
                        print('Delete =', s.peek(), 'Because',s.pop(), 'is more than', order[1])
                    else:
                        k.push(s.pop())
                while not k.isEmpty():
                    s.push(k.pop())
                    


inp = input('Enter Input : ').split(',')
s = Stack()
k = Stack()
ManageStack(inp)
print('Value in stack =',s.lst)
