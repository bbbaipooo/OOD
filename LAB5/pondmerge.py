class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

def createList(raw_list):
    head = ListNode(raw_list.pop(0))
    while len(raw_list) != 0:
        temp = ListNode(raw_list.pop(0))
        head.next = temp
    return head

def printList(LL):
    print(LL.data)
    print(LL.next.data)
    print(LL.next.next)

def size(head):
    size = 0
    node = head
    while node != None:
        node = node.next
        size += 1
    return size

def mergeOrderesList(p, q):
    for i in range():
        pass
        
L1, L2 = input("Enter 2 Lists : ").split(" ")
L1 = L1.split(",")
L2 = L2.split(",")

LL1 = createList(L1)
printList(LL1)
