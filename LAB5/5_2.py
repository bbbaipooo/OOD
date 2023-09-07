class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:  # กำหนดtailตอนที่เราจะappendกับinsertด้วย
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizes = 0

    def __str__(self):
        run = self.head
        linked = ''
        if self.isEmpty():
            return 'Empty'
        while run.next != None:
            linked += str(run.data)+' '
            run = run.next
        linked += str(run.data)
        return linked

    def reverse(self):
        run = self.tail
        linked = ''
        if self.isEmpty():
            return 'Empty'
        while run.previous != None:
            linked += str(run.data)+' '
            run = run.previous
        linked += str(run.data)
        return linked

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            run = self.head
            while run.next != None:
                run = run.next
            node.previous = run
            run.next = node
            self.tail = node
        self.sizes += 1

    def addHead(self, data):
        node = Node(data)
        node.next = self.head
        self.head.previous = node
        self.head = node
        self.sizes += 1

    def search(self, data):
        run = self.head
        while run != None:
            if run.data == data:
                return 'Found'
            run = run.next
        return 'Not Found'

    def index(self, data):
        run = self.head
        while run != None:
            if data == run.data:
                return self.size()-1
            run = run.next
        return -1

    def size(self):
        return self.sizes

    def pop(self, pos):
        run = self.head
        i = 0
        c = 0
        if pos!=999 and pos!=-999:
            while run.next != None:
                if i+1 == int(pos):
                    run.next = run.next.next  # ย้ายลูกศรชี้
                    c = 1
                run.next.previous = run  # run.nextตอนนี้ชี้ตัวถัดจากpopแล้ว-เราทำให้มันชี้กลับมา
                run = run.next  # แต่อันนี้คืการย้ายตัววิ่ง
                i += 1
        if c == 1:
            self.sizes -= 1
            c = 0
            return 'Success'
        else:
            return -1

    def insert(self, index, data):
        node = Node(data)
        run = self.head
        i = 0
        if int(index) <= 0 and int(index)!=-1:
            node.next = self.head
            self.head.previous = node
            self.head = node
        elif int(index) >= self.size() :
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        elif int(index)==-1:
            print('Test')
            while run.next != None:
                if i == int(index):
                    node.next = run.next  
                    run.next.previous = node
                    run.next = node  
                    node.previous = run
                    break
                else:
                    run = run.next
                i += 1
        else:
            while run.next != None:
                if i+1 == int(index):
                    node.next = run.next  # 2 ชี้ไปที่ตัวnode run.nextเลย
                    run.next.previous = node
                    run.next = node  # 1
                    node.previous = run
                    break
                else:
                    run = run.next
                i += 1
        self.sizes += 1


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
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("Success |", L) if k == "Success" else ("Out of Range | ", L))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
