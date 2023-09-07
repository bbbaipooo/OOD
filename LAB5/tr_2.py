class Node():
    def __init__(self,data):
        self.next=None
        self.previous=None
        self.data=data
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
            node.previous=self.tail
            self.tail=node
        self.size+=1
    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        else:
            run=self.head
            t=str(run.data)+' '
            while run.next!=None:
                run=run.next
                t+=str(run.data)+' '
            return t
    def reverse(self):
        if self.isEmpty():
            return 'Empty'
        else:
            run=self.tail
            t=str(run.data)+' '
            while run.previous!=None:
                run=run.previous
                t+=str(run.data)+' '
            return t
    def addHead(self,data):
        node=Node(data)
        if self.isEmpty():
            self.head=node
            self.previous=node
            self.tail=node   #*****************************
        else:
            node.next=self.head
            self.head.previous=node
            self.head=node
        self.size+=1
    def sizes(self):
        return self.size
    def search(self,data):
        run=self.head
        while run.data!=data:
            run=run.next
            if run==None:
                return 'Not Found'
        return 'Found'
    def index(self,data):
        run=self.head
        i=0
        while run.data!=data:
            run=run.next
            i+=1
            if run==None:
                return 'Do not have item'
        return i
    def pop(self,pos):
        if pos<0 or pos>=self.sizes():
            return 'Out of range'
        else:
            run=self.head
            if pos==0:
                run=run.next
                self.head.next=None
                run.previous=None
                self.head=run
            else:
                i=0
                while i!=(pos-1):
                    run=run.next
                    i+=1
                run.next=run.next.next
                run.next.previous=run
            self.size-=1
    def insert(self,pos,data):
        node=Node(data)
        if pos<=0:
            node.next=self.head
            self.head.previous=node
            self.head=node
        elif pos>=self.sizes():
            self.tail.next=node
            node.previous=self.tail
            self.tail=node
        else:
            i=0
            run=self.head
            while i!=(pos-1) and i<self.sizes():
                i+=1
                run=run.next
            node.next=run.next
            run.next.previous=node
            run.next=node
            node.previous=run
                
                
        self.size+=1
l=LinkedList()
l.addHead('Me')
l.append(1)
l.append('love')
l.append(3)
l.insert(3,9)
print(l)
print(l.reverse())
