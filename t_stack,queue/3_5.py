class Stack():
    def __init__(self):
        self.lst = []

    def pop(self):
        return self.lst.pop()

    def push(self, i):
        self.lst.append(i)

    def peek(self):
        return self.lst[-1]

    def size(self):
        return len(self.lst)

    def isEmpty(self):
        return self.lst == []


print("******** Parking Lot ********")
m, s, o, n = input('Enter max of car,car in soi,operation : ').split()
m, n = int(m), int(n)

car = Stack()
carB=Stack()
s = s.split(',')
for i in s:
    if i!='0':
        car.push(int(i))


if o=='arrive':
    arrive=False
    for i in s:
        if str(n) in s:
            arrive=True
        #print(str(n),'<--')
        #print(s,'<--')
    if arrive:
        print('car',n,'already in soi')
    else:
        if car.size() == m:
            print('car',n,'cannot arrive : Soi Full')
        else:
            car.push(n)
            print('car',n,'arrive! : Add Car',n)

elif o=='depart':
    depart=False
    while not car.isEmpty():
        if car.peek()==n:
            car.pop()
            print('car',n,'depart ! : Car',n,'was remove')
            depart=True
        else:
            carB.push(car.pop())
    while not carB.isEmpty():
        car.push(carB.pop())
    if depart==False:
        if car.isEmpty():
            print('car',n,'cannot depart : Soi Empty')
        else:
            print('car',n,'cannot depart : Dont Have Car',n)
print(car.lst)

