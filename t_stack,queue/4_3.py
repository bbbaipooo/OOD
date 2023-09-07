class Queue():
    def __init__(self):
        self.lst=[]
    def deQueue(self):
        return self.lst.pop(0)
    def enQueue(self,i):
        self.lst.append(i)
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return self.lst==[]

inp=input('Enter Input : ').split('/')
left=inp[0].split()
right=inp[1].split(',')
q=Queue()

for i in left:
    q.enQueue(i)

for i in right:
    order=i.split()
    if order[0]=='E':
        q.enQueue(order[1])
    elif order[0]=='D':
        q.deQueue()

duplicate=False

for i in range(q.size()):
    for j in range(i+1,q.size()):
        if q.lst[i]==q.lst[j]:
            duplicate=True
print('Duplicate') if duplicate else print('No Duplicate')
