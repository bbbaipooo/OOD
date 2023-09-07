class Stack():
    def __init__(self):
        self.list = []

    def pop(self):
        i=self.list.pop()
        return i

    def push(self,data):
        self.list.append(data)

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)

t_input = input('Enter Input : ').split(',')
s = Stack()

for i in t_input: #['A 10','A 20','A 30','P','P']
    temp = i.split() #['A','10']
    if temp[0]=='A':
        s.push(int(temp[1]))
        print('Add = ',s.peek(),' and Size = ',s.size(),sep='')
    elif temp[0]=='P':
        print('Pop = ',s.pop(),' and Index = ',s.size(),sep='')

print('Value in Stack =',s.list)


