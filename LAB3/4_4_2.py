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

q1=Queue()
q2=Queue()

t_input=input('Enter Input : ').split('/')
left=list(t_input[0].split(','))
right=list(t_input[1].split(','))


for i in right:
    i.split()
    if i[0]=='D':
        if q1.isEmpty():
            print('Empty')
        else:
            print(q1.deQueue())
    elif i[1]=='E':
        print()


