class Stack():
    def __init__(self):
        self.list = []

    def pop(self):
        i = self.list.pop()
        return i

    def push(self, data):
        self.list.append(data)
        return data

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return self.size() == 0

    def getStack(self):
        return self.list

    def peek(self):
        return self.list[-1]


def ManageStack(ll):
    for i in ll:  # ['A 10','A 20','A 30','D 20']
        order = i.split()  # ['A','10']
        if order[0] == 'A':
            print('Add =', s.push(int(order[1])))
        elif order[0] == 'P':
            if s.isEmpty():
                print(-1)
            else:
                print('Pop =', s.pop())
        elif order[0] == 'D':
            if s.isEmpty():
                print(-1)
            else:
                while not s.isEmpty():   # 10 20 30
                    if s.peek() == order[1]:
                        print('Delete =', s.pop())
                    else:
                        k.push(s.pop())
                while not k.isEmpty():
                    s.push(k.pop())
        elif order[0] == 'LD':
            if s.isEmpty():
                print(-1)
            else:
                while not s.isEmpty():
                    if order[1] > s.peek():
                        print('Delete =', s.peek(), 'Because',s.pop(), 'is less than', order[1])
                    else:
                        k.push(s.pop())
                while not k.isEmpty():
                    s.push(k.pop())
        elif order[0] == 'MD':
            if s.isEmpty():
                print(-1)
            else:
                while not s.isEmpty():
                    if s.peek() > int(order[1]):
                        print('Delete =', s.peek(), 'Because',s.pop(), 'is more than', order[1])
                    else:
                        k.push(s.pop())
                while not k.isEmpty():
                    s.push(k.pop())


ll = input('Enter Input : ').split(',')
s = Stack()
k = Stack()
ManageStack(ll)
print('Value in Stack =',s.list)
