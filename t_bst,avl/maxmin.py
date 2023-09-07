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
            print('     '*level,node.data)
            self.printTree(node.left,level+1)
   
    def insert(self,node,data):
        N=TreeNode(data)
        if self.root==None:
            self.root=N
            return self.root
        else:
            if node!=None:
                if node.data>data:
                    node.left=self.insert(node.left,data)
                else:
                    node.right=self.insert(node.right,data)
            else:
                return N
            return node
        
    def findMax(self):
        t=self.root
        while t.right:
            t=t.right
        return t.data
    
    def findMin(self):
        t=self.root
        while t.left:
            t=t.left
        return t.data

B=BST()
root=0
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
   root=B.insert(root,i)
B.printTree(root)
print('Max :',B.findMax())
print('Min :',B.findMin())
                
            