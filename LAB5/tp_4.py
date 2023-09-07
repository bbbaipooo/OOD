class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
        self.size=0
        self.isLoop=0
    def append(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            run=self.head
            while run.next!=None:
                run=run.next
            run.next=node
        self.size+=1
    def isEmpty(self):
        return self.size==0
    def __str__(self):
        if not self.isEmpty():
            run=self.head
            t=str(run.data)
            while run.next!=None:
                run=run.next
                t+='->'+str(run.data)
            return t
        return 'Empty'
    def set_next(self,index1,index2):
        if self.isEmpty():
            return 'Error! {list is empty}'
        if index1>=0 and index1<self.size:
            if index2>=0 and index2<self.size:
                i=0
                if index1>=index2:
                    self.isLoop+=1
                    cur=self.head
                    ptr=self.head
                    while i<index1:
                        cur=cur.next
                        if i<index2:
                            ptr=ptr.next
                        i+=1
                    return f'Set node.next complete, index:value = {index1}:{cur.data} -> {index2}:{ptr.data}'
                else:
                    cur=self.head
                    ptr=self.head
                    while i<index2:
                        ptr=ptr.next
                        if i<index1:
                            cur=cur.next
                        i+=1
                    cur.next=ptr
                return f'Set node.next complete, index:value = {index1}:{cur.data} -> {index2}:{ptr.data}'
            else:
                node=Node(index2)
                run=self.head
                while run.next!=None:
                    run=run.next
                run.next=node
                self.size+=1
                return f'index not in length, append : {index2}'
        else:
            return 'error'

l=LinkedList()

inp=input('Enter Input : ').split(',')
for j in inp:
    if j[:1]=='A':
        l.append(j[2:])
        print(l)
    elif j[:1]=='S':
        ind=j[2:].split(':')
        print(l.set_next(int(ind[0]),int(ind[1])))

if l.isLoop>0:
    print('Found Loop')
else:
    print('No Loop')
    print(l)