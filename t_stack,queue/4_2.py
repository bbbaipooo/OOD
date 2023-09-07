class Queue():
    def __init__(self):
        self.lst=[]
    def deQueue(self):
        return self.lst.pop(0)
    def enQueue(self,i):
        self.lst.append(i)
    def isEmpty(self):
        return self.lst==[]
    def size(self):
        return len(self.lst)

inp=input('Enter Input : ').split(',')
qN=Queue()
qS=Queue()

for i in inp:
    order=i.split()
    if order[0]=='EN':
        qN.enQueue(order[1])
    elif order[0]=='ES':
        qS.enQueue(order[1])
    elif order[0]=='D':
        if qN.isEmpty() and qS.isEmpty():
            print('Empty')
        elif not qS.isEmpty():
            print(qS.deQueue())
        elif not qN.isEmpty():
            print(qN.deQueue())