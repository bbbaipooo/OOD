class Node():
    def __init__(self, data):
        self.next = None
        self.data = data


def createLinkList(l):
    l = l.split('->')
    head = None
    for i in l:
        node = Node(i)
        if head == None:
            head = node
        else:
            run = head
            while run.next != None:
                run = run.next
            run.next = node
    return head


def printLinkList(head):
    run = head
    t = str(run.data)
    while run.next != None:
        run = run.next
        t += ' '+str(run.data)
    return t

def reverseLinkList(head):
    lst=[]
    run=head
    lst.append(run.data)
    t=''
    while run.next!=None:
        run=run.next
        lst.append(run.data)
    for i in lst[::-1]:
        t+=str(i)+' '
    return createLinkList(t)

def mergeList(p,q):
    run=p
    t=str(run.data)+' '
    while run.next!=None:
        run=run.next
        t+=str(run.data)+' '
    run=q
    while run.next!=None:
        t+=str(run.data)+' '
        run=run.next
    t+=str(run.data)
    return t

left, right = input('Enter Input (L1,L2) : ').split()
x = createLinkList(left)
y = createLinkList(right)
print(f'L1    : {printLinkList(x)}')
print(f'L2    : {printLinkList(y)}')
print(f'Merge : {mergeList(x,reverseLinkList(y))}')
