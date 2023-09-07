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


t_input = input('Enter Input : ').split('/')
left = t_input[0].split()
right = t_input[1].split(',')
memQ = Queue()

for i in left:
    memQ.enQueue(i)

for i in right:
    order = i.split()

    if order[0]=='D':
        memQ.deQueue()
    elif order[0]=='E':
        memQ.enQueue(order[1])

duplicate = False
temp = memQ.items #Queue->list

for i in range(len(temp)):
    for j in range(i+1,len(temp)):
        if temp[i] == temp[j] : duplicate = True

if duplicate: print("Duplicate")
else: print('NO Duplicate')