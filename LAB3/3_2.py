class Stack:
    # class Stack
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return True if self.size() == 0 else False

    def size(self):
        return len(self.items)

    def getStack(self):
        return self.items

    def delete(self, num) :
        self.items.remove(num)
        return num


def ManageStack(s):
    for i in t_input:
        if i[0] == 'A':
            charA, numA = i.split()
            s.push(numA)
            print('Add =', s.peek())
        elif i[0] == 'P':
            if s.isEmpty():
                print('-1')
            else:
                print('Pop =', s.pop())
        elif i[0] == 'D':
            charD, numD = i.split()
            s.push(numD)
            if s.isEmpty(): print('-1')
            else: 
                while s.size() > 0:
                    if s.peek() == numD:
                        print('Delete =', s.pop())
                    else:
                        s2.push(s.pop())

                while s2.size():
                    s.push(s2.pop())

            '''i = int(0)
            j = s.size()
            y = []
            while i < j:
                y.append(s.pop())
                i = i + 1
            print("Value in Stack = [",end='')
            while j > 0:
                j -= 1
                if j!=0: 
                    print(y[j],', ',sep='',end='')
                else:
                    print(y[j],']',sep='')'''

        elif i[0] == 'L' and i[1] == 'D':
            charLD, numLD = i.split()
            s.push(numLD)
            if s.isEmpty():
                print('-1')
            else:
                '''list=[]
                for i in s:
                    if i<numLD:
                        list.append(i)
                for j in list[::-1] :
                    while(j in s) : 
                        print("Delete =",s.delete(j),"Because",j,"is less than "+numLD)'''
                temp = s.getStack()
                del_temp_list = []
                for j in temp : 
                    if j < numLD : del_temp_list.append(j)
                for j in del_temp_list[::-1] :
                    while(j in temp) : print("Delete =",s.delete(j),"Because",j,"is less than "+numLD)
                

        elif i[0] == 'M' and i[1] == 'D':
            charMD, numMD = i.split()
            s.push(numMD)
            if s.isEmpty():
                print('-1')
            else:
                print()  # 3
    return  # (ผลในSTACK)


t_input = input('Enter Input : ').split(',')
s = Stack()
s2 = Stack()
ManageStack(s)

i = int(0)
j = s.size()
y = []
while i < j:
    y.append(s.pop())
    i = i + 1
print("Value in Stack = [",end='')
while j > 0:
    j -= 1
    if j!=0: 
        print(y[j],', ',sep='',end='')
    else:
        print(y[j],']',sep='')
