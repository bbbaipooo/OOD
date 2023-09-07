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
                if node.data>data:
                    node.left=self.insert(node.left,data)
                else:
                    node.right=self.insert(node.right,data)
            else:
                return TreeNode(data)
            return node
        
    def sum(self,node,l=[]):
        if node!=None:
            self.sum(node.left)
            l.append(node.data)
            self.sum(node.right)
            return l
            
t=BST()
root=None
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
    root=t.insert(root,i)
t.printTree(root)
ls=t.sum(root)
s=0
for i in ls:
    s+=i
print(s)