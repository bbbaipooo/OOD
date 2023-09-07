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
        elif int(index) == (self.size):
            print('Test')
            while run.next != None:
                run = run.next
            run.next = node
        else:
            while run.next != None:
                if i+1 == int(index):  # เพราะrunเชื่อมกับiเลยต้องให้ค่าiเลยก่อนrunไป
                    node.next = run.next
                    run.next = node
                    #print(run.data,end="<- \n")
                    break
                else:
                    run = run.next
                i += 1

    def isEmpty(self):
        return True if self.head == None else False

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


s = LinkedList1()
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.insert(4, 10)
# s.pop()
s.printlist()
print(s)
