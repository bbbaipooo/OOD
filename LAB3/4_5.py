class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return True if self.size() == 0 else False

    def size(self):
        return len(self.items)

    def returnQueue(self):
        return self.items

    def front(self):
        return self.items[0]

    def __str__(self):
        if self.isEmpty == True:
            return 'Empty'
        else:
            return "".join(self.items)


class Stack:
    # class Stack
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def getStack(self):
        return self.items


def reverseString(s=''):
    return s[::-1]


t_input = input('Enter Input (Normal, Mirror) : ').split()
norm = []
norm.extend(t_input[0])#['a']['b']['c']
mirr = []
mirr.extend(t_input[1])

mirr.reverse()
queueMirr=Queue(mirr)
queueNorm=Queue(norm)
stackMirr=Stack()
stackNorm=Stack()

count=1
temp=queueMirr.deQueue()
items=[]

while not queueMirr.isEmpty():
    if temp==queueMirr.front():
        count+=1
        stackMirr.push(temp)
        if count==3:
            items.append(temp)
    else:
        stackMirr.push(temp)
    temp=queueMirr.deQueue()


