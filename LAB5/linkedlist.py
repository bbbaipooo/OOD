class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            run = self.head     #runคน run.nextไอตัวรางเชื่อม
            while run.next != None:
                run = run.next
            run.next = node

    def pop(self):
        run = self.head
        while run.next.next != None:
            run = run.next
        run.next=None
        

    def printlist(self):
        run = self.head
        while run.next != None:
            print(run.data)
            run = run.next
        print(run.data)

    def __str__(self):
        return "TEST"


ll = Linkedlist()
ll.append(100)
ll.append(150)
ll.append(200)
ll.pop()
ll.printlist()
print(ll)
