class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def createList(lx=[]):  # lx same lx=[]
    lx = lx.split('->')
    head = None
    #print(len(lx))
    for i in lx:
        node = Node(i)
        if head == None:
            head = node
        else:
            run = head
            while run.next != None:
                run = run.next
            run.next = node
    return head


def printList(head):
    run = head
    item = str(run.data)+' '
    while run.next != None:
        run = run.next
        item += str(run.data)+' '
    return item

def reverseList(head):
    listN=[]
    run=head
    listN.append(str(run.data))
    while run.next!=None:
        run=run.next
        listN.append(str(run.data))
    reItem=''
    for i in range(len(listN)-1,-1,-1):
        if i==0:
            reItem+=str(listN[i])
        else:
            reItem+=str(listN[i])+'->'
    return createList(reItem)

def mergeList(x,y):
    item=''
    run=x
    item+=str(run.data)+'->'
    while run.next!=None:
        run=run.next
        item+=str(run.data)+'->'
    run=y
    while run.next!=None:
        item+=str(run.data)+'->'
        run=run.next
    item+=str(run.data)
    return createList(item)
        
        



l1, l2 = input('Enter Input (L1,L2) : ').split()
a = createList(l1)
b = createList(l2)
print('L1    :', printList(a))
print('L2    :', printList(b))
print('Merge :',printList(mergeList(a,reverseList(b))))
