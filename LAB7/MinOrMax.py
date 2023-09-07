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
            print("    "*level,node.data)
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
        
    def findMin(self):
        t=self.root
        while t.left!=None:
            t=t.left
        return t.data
    
    def findMax(self):
        t=self.root
        while t.right!=None:
            t=t.right
        return t.data
    
    def findList(self,node,l=[]):
        if node!=None:
            self.findList(node.left)
            l.append(node.data)
            self.findList(node.right)
            return l
        
            
            

B=BST()
root=None
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
    root=B.insert(root,i)
B.printTree(root)
print('--------------------------------------------------')
print(f'Min : {B.findMin()}')
print(f'Max : {B.findMax()}')
dream=B.findList(root)
print(f'Min : {dream[0]}')
print(f'Max : {dream[-1]}')