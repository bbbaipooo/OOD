class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        if len(self.items)>0:
            return self.items.pop(0)
    def copy(self,i):
        self.items = i
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def returnQueue(self):
        return self.items
    def insertQueue(self,data,mark):
        self.temp = []
        for i in range(mark):
            self.temp.append(self.items[i])
        self.temp.append(data)
        for i in range (mark,len(self.items)):
            self.temp.append(self.items[i])
        self.items = self.temp
q1 = Queue()
q2 = Queue()
t_input = input("Enter Input : ").split('/')
left = list(t_input[0].split(','))
right = list(t_input[1].split(','))
for i in right:
    l = i.split()
    if l[0] == 'D':
        if q1.size() == 0:
            print("Empty")
        else:
            q2.deQueue()
            print(q1.deQueue())
    elif l[0] == 'E':
        for j in left:
            t = j.split()
            if t[1]==l[1]:
                mark = q1.size()
                for ID in range(q2.size()-1,-1,-1):
                    if q2.returnQueue()[ID] == t[0]:
                        mark = ID+1
                        break
                if mark == q1.size():
                    q1.enQueue(t[1])
                    q2.enQueue(t[0])
                else:
                    q1.insertQueue(t[1],mark)
                    q2.insertQueue(t[0],mark)