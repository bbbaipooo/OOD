class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    def __str__(self):
        return str(self.data)


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level+1)
            print('     '*level, node)
            self.printTree(node.left, level+1)

    def insert(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            r = self.root
            while True:
                if r.data > data:
                    if not r.left:
                        r.left = node
                        break
                    else:
                        r = r.left
                else:
                    if not r.right:
                        r.right = node
                        break
                    else:
                        r = r.right
                        
def preOrder(node):
    if node!=None:
        print(node,end=' ')
        preOrder(node.left)
        preOrder(node.right)
        
def postOrder(node):
    if node!=None:
        postOrder(node.left)
        postOrder(node.right)
        print(node,end=' ')

def inOrder(node): #data : least to max
    if node!=None:
        inOrder(node.left)
        print(node,end=' ')
        inOrder(node.right)
        
'''def Breadth(node,q=[]):
    q.append(node)
    while q:
        print(q.pop(0))
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)'''
def bfs(node,q = []):
    if node != None:
        print(node,end=" ")
        if node.left!=None:q.append(node.left)
        if node.right!=None:q.append(node.right)
        if len(q)!=0:bfs(q.pop(0),q)
        else:return
    
    
        
                        
tree=BinarySearchTree()
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
    tree.insert(i)
#tree.printTree(tree.root)

print('Preorder : ',end='')
preOrder(tree.root)
print('\n','Inorder : ',end='',sep='')
inOrder(tree.root)
print('\n','Postorder : ',end='',sep='')
postOrder(tree.root)
print('\n','Breadth : ',end='',sep='')
bfs(tree.root)
