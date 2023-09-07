class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def isEmpty(self):
        return self.size==0
    def append(self,data):
        node=Node(data)
        if self.isEmpty():
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        self.size+=1
    def __str__(self):
        if not self.isEmpty():
            run=self.head
            t=str(run.data)
            while run.next!=None:
                run=run.next
                t+=' <- '+str(run.data)
            return t
        return 'Empty'
l=LinkedList()
nl=LinkedList()
print(' *** Locomotive ***')
inp=input('Enter Input : ').split()

num=0
numBer=0
for i in inp:
    l.append(i)
    if i=='0':
        numBer=num
    num+=1
print('Before :',l)


for i in inp[numBer::]:
    nl.append(i)
if numBer>0:
    for i in inp[:numBer:]:
        nl.append(i)
print('After :',nl)