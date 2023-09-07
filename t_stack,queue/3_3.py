class Stack():
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return self.list == []

    def size(self):
        return len(self.list) 

def postFixeval(st):
    s = Stack()
    for i in st:
        if i == '+':
            a = s.pop()
            b = s.pop()
            c = float(b)+float(a)
            s.push(c)
        elif i == '-':
            a = s.pop()
            b = s.pop()
            c = float(b)-float(a)
            s.push(c)
        elif i == '*':
            a = s.pop()
            b = s.pop()
            c = float(b)*float(a)
            s.push(c)
        elif i == '/':
            a = s.pop()
            b = s.pop()
            c = float(b)/float(a)
            s.push(c)
        else:
            s.push(i)

    return s.pop()


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())


print("Answer : ",'{:.2f}'.format(postFixeval(token)))


