class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def createList(list=[]):
    Head = None
    list = list.split('->')
    # print(len(list))
    for i in list:
        node = Node(i)
        if Head == None:
            Head = node
        else:
            run = Head
            while run.next != None:
                run = run.next
            run.next = node
    return Head


def printList(Head):
    run = Head
    item = str(run.data)+' '
    while run.next != None:
        run = run.next
        item += str(run.data)+' '
    return item

def reverseList(Head):
    list = []
    run = Head
    list.append(str(run.data))
    while run.next != None:
        run = run.next
        list.append(str(run.data))
    item = ''
    for i in range(len(list)-1, -1, -1):
        if i == 0:
            item += str(list[i])
        else:
            item += str(list[i])+'->'
    return createList(item)

def mergeList(a, b):
    list = ''
    run = a
    list += str(run.data)+'->'
    while run.next != None:
        run = run.next
        list += str(run.data)+'->'
    run = b
    list += str(run.data)+'->'
    while run.next != None:
        run = run.next
        list += str(run.data)+'->'
    return createList(list)
 

l1, l2 = input('Enter Input (L1,L2) : ').split()
x = createList(l1)
y = createList(l2)
print('L1    : ', printList(x))
print('L2    : ', printList(y))
print('Merge : ', printList(mergeList(x, reverseList(y))))
