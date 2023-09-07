class Queue():
    def __init__(self):
        self.lst=[]
    def deQueue(self):
        return self.lst.pop(0)
    def enQueue(self,i):
        self.lst.append(i)
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return self.lst==[]

inp=input('Enter Input : ').split('/')
left=inp[0].split()
right=inp[1].split(',')
q=Queue()

for i in left:
    q.enQueue(i)

for i in right:
    order=i.split()
    if order[0]=='E':
        q.enQueue(order[1])
    elif order[0]=='D':
        q.deQueue()

duplicate=False
temp=q.lst

for i in range(len(temp)):
    for j in range(i+1,len(temp)):
        if temp[i]==temp[j]:duplicate=True
print('Duplicate')if duplicate else print('No Duplicate')

'''for i in temp:                                              # <-----วิะีนี้ NO!!!!!!!!!!
    for j in temp[1::]: #ปกติก้จะไปrunที่index=1เลย แต่ว่าอันนี้ไม่มันไปrunที่index=0เหมือนiเพราะมันมีtempตัวดีกัน มันเลยวรแบบparallel
        if i==j:
            print(i,j)
            duplicate=True
print('Duplicate')if duplicate else print('No Duplicate')'''