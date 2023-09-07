class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BST():
    def __init__(self):
        self.root=None
    
    def printTree(self,node,level=0):
        if node!=None:
            self.printTree(node.right,level+1)
            print('    '*level,node.data)
            self.printTree(node.left,level+1)
    
    def insert(self,node,data):
        if self.root==None:
            self.root=TreeNode(data)
            return self.root
        else:
            if node!=None:
                if data<node.data:
                    node.left=self.insert(node.left,data)
                else:
                    node.right=self.insert(node.right,data)
            else:
                return TreeNode(data)
            return node
        
def inorder(node):
    if node!=None:
        inorder(node.left)
        print(f'{node.data} ',end='')
        inorder(node.right)
        
def preorder(node):
    if node!=None:
        print(f'{node.data} ',end='')
        preorder(node.left)
        preorder(node.right)
        
def postorder(node):
    if node!=None:
        postorder(node.left)
        postorder(node.right)
        print(f'{node.data} ',end='')

def Breadth(node,q=[]):
    if node!=None:
        print(node.data,end=' ')
        if node.left:Breadth(q.append(node.left))
        if node.right:Breadth(q.append(node.right))
        if len(q):Breadth(q.pop(0))
        else:return
        
    
        
        
        
t=BST()
root=None
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
    root=t.insert(root,i)
t.printTree(root)
print('Preorder : ',end='')
preorder(root)
print('')
print('Inorder : ',end='')
inorder(root)
print('')
print('Postorder : ',end='')
postorder(root)
print('')
print('Breadth : ',end='')
Breadth(root)
                