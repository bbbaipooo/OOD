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
    def mul3(self,node,data):
        if node!=None:
            self.mul3(node.left,data)
            if node.data>data:
                node.data=node.data*3
            self.mul3(node.right,data)
        
        
        
B=BST()
root=None
inp1,inp2=input('Enter Input : ').split('/')
inp1=list(map(int,inp1.split()))
inp2=int(inp2)
print(inp1)
for i in inp1:
    root=B.insert(root,i)
B.printTree(root)
B.mul3(root,inp2)
print('--------------------------')
B.printTree(root)