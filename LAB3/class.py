from re import A


class Stack():
    def __init__(self):
        self.lst=[]
    
    def push(self,x):
        self.lst.append(x)

    def pop(self):
        a=self.lst[-1]
        del self.lst[-1]
        return a

    def peek(self):
        return self.lst[-1]

    def size(self):
        return len(self.lst)

    def isEmpty(self):
        return True if self.size()==0 else False

class Queue():
    def __init__(self):
        self.lst=[]

    def deQueue(self):
        a=self.lst[0]
        del self.lst[0]
        return a

    def enQueue(self,x):
        self.lst.append(x)
