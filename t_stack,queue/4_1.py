class Queue():
    def __init__(self):
        self.lst=[]
    def deQueue(self):
        return self.lst.pop(0)
    def enQueue(self,i):
        self.lst.append(i)
    def size(self):
        return len(self.lst)

inp=input('Enter Input : ').split(',')
q=Queue()

for i in inp:
    order=i.split()
    if order[0]=='E':
        q.enQueue(order[1])
        print('Add',order[1],'index is',q.size()-1)
    elif order[0]=='D':
        print('Pop',q.deQueue(),'size in queue is',q.size())
print('Number in Queue is :',q.lst)

