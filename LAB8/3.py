class BST:
    def __init__(self):
        self.root = None
    def setRoot(self,node):
        self.root = node
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        elif self.root != None:
            p=self.root
            while(p!=None):
                if data >= p.data:
                    if p.right == None:
                        p.right = Node(data)
                        break
                    p=p.right

                elif data < p.data:
                    if p.left == None:
                        p.left = Node(data)
                        break
                    p=p.left
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

def findRank(node,value):
    global rank
    global ans
    global found
    if node == None:
        return
    findRank(node.left,value)
    rank+=1
    #print('data : ' + str(node.data) +' rank : ' + str(rank))
    if node.data == value:
        if not found:
            ans = rank-1
            return
    elif node.data > value:
        if not found:
            found = True
            #print('elif : ' + str(node.data) + ' rank : ' + str(rank))
            ans = rank-1
            return
    findRank(node.right,value)
    if not found:
        ans=rank

inp,val=input('Enter Input : ').split('/')
inpLis = [int(e) for e in inp.split()]
ans=0
rank=0
found = False
T = BST()
for data in inpLis:
    T.insert(data)
T.printTree(T.root)
findRank(T.root,int(val))
print('--------------------------------------------------')
print('Rank of {0} : '.format(val) + str(ans))