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
        
    def findPaPa(self,data):
        r=self.root
        if r.data==data:
            return f'None Because {data} is Root'
        else:
            while True:
                if not r.right and not r.left:
                    return 'Not Found Data'
                elif r.data<data and r.right.data==data:
                    return r.data
                elif r.data>data and r.left.data==data :
                    return r.data
                
                if data<r.data:
                    r=r.left
                else:
                    r=r.right
        
B=BST()
root=None
inp1,inp2=input('Enter Input : ').split('/')
inp1=list(map(int,inp1.split()))
inp2=int(inp2)

for i in inp1:
    root=B.insert(root,i)
B.printTree(root)
print(B.findPaPa(inp2))
    
                