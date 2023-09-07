class stack():
    def __init__(self):
        self.lst=[]
    def isEmpty(self):
        return True if self.lst==[] else False
    def push(self,data):
        self.lst.append(data)
    def pop(self):
        return self.lst.pop(-1)
    def isSize(self):
        return len(self.lst)
    def peek(self):
        return self.lst[-1]
    
s=stack()
inp=input('Enter Stack : ').split()
for i in inp:
    s.push(i)
    print(s.peek(),end=' ')
print()
print(s.lst)