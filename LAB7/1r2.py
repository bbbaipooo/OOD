class TreeNode():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        
class BST():
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        node=TreeNode(data)
        if self.root==None:
            self.root=node
            return
        else:
            r=self.root
            while True:
                if data<r.data:
                    if r.left==None:
                        r.left=node
                        return
                    else:
                        r=r.left
                else:
                    if r.right==None:
                        r.right=node
                        return 
                    else:
                        r=r.right
        
    def printTree(self,node,level=0):
        if node!=None:
            self.printTree(node.right,level+1)
            print('     '*level,node.data)
            self.printTree(node.left,level+1)
            
t=BST()
inp=list(map(int,input('Enter input : ').split()))
for i in inp:
    t.insert(i)
t.printTree(t.root)