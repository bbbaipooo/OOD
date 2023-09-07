class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if self.head == None:
            return "Empty"
        else:
            items = ""
            Run = self.head
            while Run.next != None:
                items += str(Run.data) + " "
                Run = Run.next
            items += str(Run.data)
            return items
        
    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            run = self.head
            while run.next != None:
                run = run.next
            run.next = node
        self.size += 1
        
    def pop(self):
        if self.head==None:
            return 'Empty'
        else:
            run=self.head
            while run.next.next!=None:
                run=run.next
            run.next=None
        self.size-=1
        
    
        
l=LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.pop()
print(l)
        
    