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


t_input = input('Enter Input : ').split(',')
nQ = Queue()
sQ = Queue()

for i in t_input:
    order = i.split()

    if order[0]=='ES':
        sQ.enQueue(order[1])
    elif order[0]=='EN':
        nQ.enQueue(order[1])
    elif order[0]=='D':
        if nQ.isEmpty() and sQ.isEmpty():
            print('Empty')
        elif sQ.isEmpty()!=1:
            print(sQ.deQueue())
        else:
            print(nQ.deQueue())

