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
        data=int(data)
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
        
    def checkpos(self,data):
        node=TreeNode(data)
        if self.root.data==data:
            return 'Root'
        else:
            r=self.root
            while True:
                if data<r.data:
                    r=r.left
                else:
                    r=r.right
                    
                if not r.left and not r.right and r.data==data:
                    return "Leaf"
                elif r.data==data:
                    return "Inner"
                elif not r.left and not r.right:
                    return "Not exist"
                    
                
            
            
        
t=BST()
root=None
inp=list(map(int,input('Enter Input : ').split()))
for i in inp[1::]:
    root=t.insert(root,i)
t.printTree(root)
print(t.checkpos(inp[0]))