class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return True if self.size() == 0 else False
    def size(self):
        return len(self.items)
    def returnQueue(self):
        return self.items

t_input=input('Enter Input : ').split(',')
q=Queue()

for i in t_input:
    if i[0]=='E':
        index=q.size()
        char,num=i.split()
        q.enQueue(num)
        print('Add',num,'index is',index)
    elif i[0]=='D':
        if q.isEmpty():
            print('-1')
        else:
            print('Pop',q.deQueue(),'size in queue is',q.size())

if q.isEmpty():
    print('Empty')
else:
    print('Number in Queue is :  [',end='')
    while q.size()>0:
        if q.size()==1:
            print('\'',q.deQueue(),'\'',sep='',end='')
        else:
            print('\'',q.deQueue(),'\', ',sep='',end='')
    print(']')