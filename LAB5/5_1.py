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
                if i+1 == int(index):  # เพราะrunเชื่อมกับiเลยต้องให้ค่าiเลยก่อนrunไป  0 1 2 3
                    node.next = run.next
                    run.next = node
                    #print(run.data,end="<- \n")
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



t_input = input('Enter Input : ').split(',')
linked = LinkedList1()

left = t_input[0].split()
for i in left:
    linked.append(i)

for i in list(t_input)[1::]:
    right = i.split(':')
    if linked.isEmpty():
        print('List is empty')
        if int(right[0])==0:
            linked.insert(right[0],right[1])
            print('index = ', right[0], ' and data = ', right[1],sep='')
        else: 
            print('Data cannot be added')
    else:
        print('link list :', linked)
        if int(right[0])>=0 and int(right[0])<=linked.sizes():####
            linked.insert(right[0],right[1])
            print('index = ', right[0].strip(' '), ' and data = ', right[1],sep='')########
        else:
            print('Data cannot be added')

if not linked.isEmpty():
    print('link list :', linked)
else:
    print('List is empty')
