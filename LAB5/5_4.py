class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.sizes = 0
        self.count = 0

    def size(self):
        return self.sizes

    def isEmpty(self):
        return True if self.sizes == 0 else False

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            run = self.head
            while run.next != None:
                run = run.next
            run.next = node
        self.sizes += 1

    def __str__(self):
        if not self.isEmpty():
            run = self.head
            item = ''
            while run.next != None:
                item += str(run.data)+'->'
                run = run.next
            item += str(run.data)
            return item
        return 'Empty'

    def set_next(self, index1, index2):
        if self.isEmpty():
            return 'Error! {list is empty}'
        elif index1 > self.size()-1:
            return 'Error! {index not in length}: '+str(index1)
        elif index2 > self.size()-1:
            self.append(str(index2))
            return 'index not in length, append : '+str(index2)

        if index1 < index2:
            i = 0
            cur = self.head
            ptr = self.head
            while i < index2:
                if i < index1:
                    cur=cur.next
                ptr=ptr.next
                i+=1
            cur.next=ptr
            return f'Set node.next complete!, index:value = {index1}:{cur.data} -> {index2}:{ptr.data}'
        
        elif index2<index1:
            self.count+=1
            i=0
            cur=self.head
            ptr=self.head
            while i<index1:
                if i<index2:
                    cur=cur.next
                ptr=ptr.next
                i+=1
            #ptr.next=cur
            return f'Set node.next complete!, inidex:value = {index1}:{ptr.data} -> {index2}:{cur.data}'

        elif index1==index2:
            self.count+=1
            cur=self.head
            i=0
            while i<index1:
                cur=cur.next
                i+=1
            return f'Set node.next complete!, index:value = {index1}:{cur.data} -> {index2}:{cur.data}'
            
inp = input('Enter input : ').split(',')
L = LinkedList()
for i in inp:
    order = i.split()
    if order[0] == 'A':
        L.append(int(order[1]))
        print(L)
    elif order[0] == 'S':
        temp=order[1].split(':')
        print(L.set_next(int(temp[0]),int(temp[1])))
        
if L.count==0:
    print('No Loop')
    print(L)
elif L.count>0:
    print('Found Loop')
