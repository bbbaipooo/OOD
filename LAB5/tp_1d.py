from asyncio.windows_events import NULL


class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Linkedlist():
    def __init__(self):
        self.head=None
    def append(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            run=self.head
            while run.next!=None:
                run=run.next
            run.next=node
    def isEmpty(self):
        return True if self.head==None else False
    def __str__(self):
        if not self.isEmpty():
            run=self.head
            t=''
            while run.next!=None:
                t+=str(run.data)+'<-'
                run=run.next
            t+=str(run.data)
            return t
l=Linkedlist()
a=Linkedlist()
inp=input('Enter Input : ').split()
for i in inp:
    l.append(i)
print(f'Before : {l}')
for i in range(len(inp)):
    if int(inp[i])==0:
        num=i
        for j in inp[i::]:
            a.append(j)
        if num>0:
            for k in inp[0:num:]:
                a.append(k)
print(f'After : {a}')
            

