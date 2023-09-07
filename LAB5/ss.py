class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList1:
    def __init__(self):
        self.head = None
        self.size = 0

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
        run = self.head
        while run.next.next != None:
            run = run.next
        run.next = None
        self.size -= 1

    def insert(self, index, data):
        node = Node(data)
        run = self.head
        i = 0
        if int(index) == 0:
            node.next = self.head
            self.head = node
        elif int(index) == self.size: 
            while run.next != None:
                run = run.next
            run.next = node
        else:
            while run.next != None:
                if i+1 == int(index):  
                    node.next = run.next
                    run.next = node
                    break
                else:
                    run = run.next
                i += 1
        self.size+=1

    def isEmpty(self):
        return self.head == None 

    def printlist(self):
        run = self.head
        while run.next != None:
            print(run.data)
            run = run.next
        print(run.data)

    def __str__(self):
        run = self.head
        items = ''
        while run.next != None:
            items += str(run.data)
            items += '->'
            run = run.next
        items += str(run.data)
        return items

    def sizes(self):
        return self.size