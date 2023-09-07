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
        
    def height(self,node):
        if node==None:
            return -1
        else:
            return max(self.height(node.left),self.height(node.right))+1
        
t=BST()
root=None
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
    root=t.insert(root,i)
t.printTree(root)
if t.height(root)>0:
    print(f'Height = {t.height(root)}')
else:
    print('No Height')