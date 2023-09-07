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
        return self.items == []

    def size(self):
        return len(self.items)


def carAlreadyInSoi(nInStr):
    for i in range(len(s)):
        if nInStr == s[i]:
            return 1
    return 0


def departCar(nInStr):
    for i in range(s1.size()):  # ต้องใช้เป็นlenเพราะเราต้องการวนให้ครบทุกสมาชิกในstack s1 ถ้าเราใช้ให้มันวนในs1เลยพอเราดึงpopออกมันจะเคลื่อนในตัวstackแล้วจะรวน
        if s1.peek() == nInStr:
            s1.pop()
        else:
            s2.push(s1.pop())
    if s2.size() != 0:
        for i in range(s2.size()):
            s1.push(s2.pop())


print("******** Parking Lot ********")

# m=max , s=member car in soi , o=arrive/depart , n=car(depart/arrive)
m, s, o, n = input("Enter max of car,car in soi,operation : ").split()

nInStr = n
m, n = int(m), int(n)
s = list(s.split(','))

s1 = Stack()
s2 = Stack()

carAlready = carAlreadyInSoi(nInStr)

for i in range(len(s)):  # Car : list -> stack
    if s[0] != '0':  # ถ้า0ไม่ต้องใส่ให้stack empty
        s1.push(s.pop(0))
        
if s1.size() == m : # Car Full?
    if o=='depart':
        departCar(nInStr)
        print('car', n, 'depart ! : Car',n,'was remove')
    else:
        print('car', n, 'cannot arrive : Soi Full')
else:
    if carAlready:  # มีรถคันนี้อยู่แล้วมั้ย
        if o == 'arrive':
            print('car', n, 'already in soi')
        elif o == 'depart':
            departCar(nInStr)
            print('car', n, 'depart ! : Car',n,'was remove')
    else:
        if o=='arrive':
            s1.push(n)
            print('car', n, 'arrive! : Add Car',n)
        elif o=='depart':
            if s1.isEmpty():
                print('car',n,'cannot depart : Soi Empty')
            else:
                print('car',n,'cannot depart : Dont Have Car 1')

i = int(0)
j = s1.size()
y = []
while i < j:
    y.append(s1.pop())
    i = i + 1
print('[', end='')
while j > 0:
    # นอกจากจะลบค่าjในการวนลูปแล้วยังเปลี่ยนจากค่าsizeให้เป็นindexด้วย : เลยต้องเอาไว้ก่อนที่จะy[j]ไม่งั้นจะทำให้idex out of range
    j -= 1
    if j == 0:  # ตัวสุดท้าย
        print(y[j], end='')
    else:
        print(y[j], ", ", sep='', end='')
print(']', end='')


'''
showข้อมูลในstack

i = int(0)
j = s1.size()
y = []
while i < j:
    y.append(s1.pop())
    i = i + 1
print("Value in Stack =",end='')
while j > 0:
    j -= 1
    print("",y[j],end='')

'''
