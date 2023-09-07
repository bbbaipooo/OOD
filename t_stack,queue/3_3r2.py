class Stack():
    def __init__(self):
        self.lst=[]
    def pop(self):
        return self.lst.pop()
    def push(self,i):
        self.lst.append(i)
    def peek(self):
        return self.lst[-1]
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return self.lst==[]

def postFixeval(st):
    s=Stack()
    for i in st:
        if i=='+':
            a=s.pop()
            b=s.pop()
            c=b+a
            s.push(c)
        elif i=='-':
            a=s.pop()
            b=s.pop()
            c=b-a
            s.push(c)
        elif i=='*':
            a=s.pop()
            b=s.pop()
            c=b*a
            s.push(c)
        elif i=='/':
            a=s.pop()
            b=s.pop()
            c=b/a
            s.push(c)
        else:
            s.push(float(i))

    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

print("Answer : ",'{:.2f}'.format(postFixeval(token)))