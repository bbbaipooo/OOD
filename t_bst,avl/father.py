class TreeNode():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        
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
def checkDad(root,data):
    t=root
    if t.data==data:
        return 'No Dad'
    else:
        while True:
            if not t.left and not t.right:
                return 'Not Have'
            if t.data>data and t.left.data==data:
                return t.data
            elif t.data<data and t.right.data==data:
                return t.data
            
            
            if t.data>data:
                t=t.left
            elif t.data<data:
                t=t.right

B=BST()
root=None
inp1,inp2=input('Enter Input : ').split('/')
inp1=list(map(int,inp1.split()))
inp2=int(inp2)
for i in inp1:
    root=B.insert(root,i)
B.printTree(root)
print(checkDad(root,inp2))