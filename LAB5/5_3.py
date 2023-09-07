class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.sizes = 0

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.sizes=1
        else:
            run = self.head
            while run.next != None:
                run = run.next
            run.next = node
            self.sizes += 1

    def isEmpty(self):
        return True if self.size == 0 else False

    def pop(self):
        if self.size() == 1:
            i = self.head
            self.head = None
            self.sizes = 0
            return i
        elif self.size()==2:
            run=self.head
            i=run.next
            run.next=None
            self.sizes=1
            return i
        elif self.size()>1:
            run = self.head
            while run.next.next != None:
                run = run.next
            i = run.next
            run.next = None
            self.sizes -= 1
            return i
        

    def size(self):
        return self.sizes

    def __str__(self):
        item = ''
        if self.size()>1:
            run = self.head
            while run.next != None:
                item += str(run.data)+' '
                run = run.next
            item += str(run.data)+' '
            return item
        elif self.size()==1:
            return str(self.head.data)
        else:
            return item
        


inp = input('Enter Input (L1,l2) : ').split()

l1 = inp[0].split('->')
l2 = inp[1].split('->')

ll1 = LinkedList()
ll2 = LinkedList()

for i in l1:
    ll1.append(i)
for i in l2:
    ll2.append(i)

print('L1    :', ll1)
print('L2    :', ll2)

while not ll2.isEmpty():
    ll1.append(ll2.pop())

print('Merge :', ll1)
