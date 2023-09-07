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

    def __str__(self):
        if self.isEmpty == True:
            return 'Empty'
        else :
            return "".join(self.items)

t_input=input('Enter Input : ').split('/')
left=t_input[0].split(',')
right=t_input[1].split(',')

fQ=Queue()
sQ=Queue()

# for i in left:
#     order1=i.split()

#     if order1[0]=='1':
#         fQ.enQueue(order1[1])
#     elif order1[0]=='2':
#         sQ.enQueue(order1[1])

for i in right:
    order2=i.split()

    if order2[0]=='D':
        if fQ.isEmpty() and sQ.isEmpty():
            print('Empty')
        elif fQ.isEmpty()!=1:
            print(fQ.deQueue())
        else :
            print(sQ.deQueue())
    elif order2[0]=='E':
        if order2[1][0]=='1':
            fQ.enQueue(order2[1])
        elif order2[1][0]=='2':
            sQ.enQueue(order2[1])
    