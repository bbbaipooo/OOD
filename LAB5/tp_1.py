class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
        self.size=0
    def isEmpty(self):
        return True if self.size==0 else False
    def append(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            run=self.head
            while run.next!=None:
                run=run.next
            run.next=node
        self.size+=1
    def insert(self,index,data):
        node=Node(data)
        if int(index)==0:   #******indexที่รับเข้ามาเป็นchar
            node.next=self.head
            self.head=node
        elif int(index)==self.size:
            run=self.head
            while run.next!=None:
                run=run.next
            run.next=node
        elif int(index)>=0 and int(index)<self.size:
            run=self.head
            i=0
            while i<(int(index)-1):
                run=run.next
                i+=1
            if run.next!=None:
                node.next=run.next #ตอนแรกใช้node.next=run.next.nextอย่างงั้นมันไม่ได้ชี้ตัวต่อไปแต่ชี้ตัวต่อๆไปทำให้มันไปชี้ข้อมูลตัวถัดถัดไปแทนที่จะเป็นตัวถัดไป
            run.next=node
        elif int(index)>=self.size or int(index)<0:
            return False
        self.size+=1
    def __str__(self):
        if not self.isEmpty():
            run=self.head
            t=''
            while run.next!=None:
                t+=str(run.data)+'->'
                run=run.next
            t+=str(run.data)
        return t
        
inp=input('Enter Input : ').split(',')
d=inp[0].split()
l=LinkedList()
for i in d:
    l.append(i)
print('link list :',l)
for i in inp[1::]:
    order=i.split(':')
    l.insert(order[0],order[1])
    idx=order[0].strip(' ')
    if int(order[0])>l.size or int(order[0])<0:
        print('Data can not be added')
    else:print(f'index = {idx} and data = {order[1]}')
    print('link list :',l)