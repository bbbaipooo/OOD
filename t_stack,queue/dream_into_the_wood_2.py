class Stack():
    def __init__(self):
        self.lst=[]
    
    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def push(self,i):
        self.lst.append(i)

    def isEmpty(self):
        return self.lst==[]

    def size(self):
        return len(self.lst)

    def clear(self):
        self.lst=[]

T=Stack()
S=Stack()
inp=input('Enter Input : ').split(',')

for i in inp:
    order=i.split()
    if order[0]=='A':
        T.push(order[1])
    elif order[0]=='B':
        if T.isEmpty():
            print(0)
        else:
            S.push(T.pop())
            i=1
            while T.size()>0:
                if int(S.peek())<int(T.peek()):      #strเทียบstr Asciiเทียบแค่ตัวเดียว มันคือการเทียบchar ex.10 มันก้เทียบแค่1 !!!!!!!!!!!!!!
                    print('[]',S.peek())
                    S.push(T.pop())
                    i+=1    
                else:
                    T.pop()
            print(i)
       