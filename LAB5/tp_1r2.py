class Node():
    def __init__(self,data):
        self.next=None
        self.data=data
class LinkedList():
    def __init__(self):
        self.head=None
        self.size=0
        self.tail=None
    def isEmpty(self):
        return self.size==0
    def append(self,data):
        node=Node(data)
        if self.isEmpty():
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node     #******************************
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
    def addHead(self,data):
        node=Node(data)
        if self.isEmpty():
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node
        self.size+=1
    def search(self,data):
        if self.isEmpty():
            return 'Empty'
        run=self.head
        while run.data!=data:
            run=run.next
            if run==None:
                return 'Not Found'
        return 'Found'
    def index(self,data):
        if self.isEmpty():
            return -1
        i=0
        run=self.head
        while run.data!=data:
            run=run.next
            i+=1
            if run==None:
                return -1
        return i
    def sizes(self):
        return self.size 
    def pop(self,pos):
        run=self.head
        if pos<0 or pos>=self.sizes():
            return 'Out of Range'
        elif pos==0:
            self.head=run.next
            run.next=None
            return 'Success'
        elif pos==(self.sizes()-1):
            while run.next.next!=None:
                run=run.next
            run.next=None
            self.tail=run
            return 'Success'
        else:
            i=0
            while i!=(pos-1):
                run=run.next
                i+=1
            run.next=run.next.next
            return 'Success'
                    
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.sizes(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)