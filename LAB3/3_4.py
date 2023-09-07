class Stack:

    """class Stack
        default : empty stack / Stack([...])
    """
    total = 0

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
        Stack.total += 1

    def __str__(self):
        s = 'stack of'+str(self.size())+'items'
        for ele in self.items:
            s += str(ele)+''
        return s

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


print(' ***Infix to Postfix***')

inp = input('Enter Infix expression : ')
S = Stack()

opdict = {
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '(':3,
    '^':4
    }
print('PostFix : ')
for ch in inp:
    if ch.isalpha():
        print(ch,end="")
        continue
    if ch==')':
        while S.peek() != '(':
            print(S.pop(),end="")
        S.pop()

    elif not S.isEmpty() and (ch=='(' or opdict[ch] > opdict[S.peek()]) :
        S.push(ch)

    else :
        while (not S.isEmpty() and S.peek() != '(') and opdict[ch] <= opdict[S.peek()]:
            print(S.pop(),end="")
        S.push(ch)

while not S.isEmpty():
    print(S.pop(), end='')

print()