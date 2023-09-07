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
    def checkPos(self,data):
        t=self.root
        if t.data==data:
            return "Root"
        else:
            while True:
                if t.data>data:
                    t=t.left
                else:
                    t=t.right
                    
                if t.data==data and not t.left and not t.right:
                    return "Leaf"
                elif t.data==data:
                    return "Inner"
                elif not t.left and not t.right:
                    return "Not exist"
        
B=BST()
root=None
inp1,inp2=input('Enter Input : ').split('/')
inp1=list(map(int,inp1.split()))
print(inp1)
for i in inp1:
    root=B.insert(root,i)
B.printTree(root)
print(B.checkPos(int(inp2)))

            