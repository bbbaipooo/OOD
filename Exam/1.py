class Stack :
    def __init__(s) :    
        s.items = []

    def push(s,i):       
        s.items.append(i)

    def pop(s) :      
        return s.items.pop()

    def isEmpty(s) : 
        if s.items == [] :
            return True
        else :
            return False

    def peek(s) :       
        return s.items[-1]

    def bottom(s) :
        return s.items[0] 


    def size(s) :     
        return len(s.items)

    def __str__(self):
        if not self.isEmpty():
            Data = "Data in Stack is : "
            for item in self.items:
                Data += str(item)+' '
            return Data
        return 'Empty'

inp = int(input("Enter choice : "))
if(inp == 1):
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())

elif(inp == 2):
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())

else :
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())
