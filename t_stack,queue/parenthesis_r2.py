class Stack():
    def __init__(self):
        self.lst=[]
    def pop(self):
        return self.lst.pop()
    def push(self,i):
        self.lst.append(i)
    def peek(self):
        return self.lst[-1]
    def isEmpty(self):
        return self.lst==[]
    def size(self):
        return len(self.lst)

def isParenthesis(inp):
    s=Stack()
    opn='([{'
    cls=')]}'
    for i in inp:
        if i in opn:
            s.push(i)
        elif i in cls:
            if s.isEmpty():
                return 'close paren is excess'
            elif opn.index(s.peek())==cls.index(i):
                s.pop()
            else:
                return 'not matching'
    if not s.isEmpty():
        return 'open paren is excess'
    return 'matching'
    
inp=input('Enter Input : ')
print(isParenthesis(inp))
        