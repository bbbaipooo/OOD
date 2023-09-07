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
        
    def inorder(self,node):
        if node!=None:
            self.inorder(node.left)
            print(f'{node.data } ',end='')
            self.inorder(node.right)
            
    def preorder(self,node):
        if node!=None:
            print(f'{node.data} ',end='')
            self.preorder(node.left)
            self.preorder(node.right)
                
    def postorder(self,node):
        if node!=None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(f'{node.data} ',end='')
            
    def BFS(self,node,q=[]):
        if node!=None:
            print(node.data,end=' ')
            if node.left:q.append(node.left)
            if node.right:q.append(node.right)
            if len(q):self.BFS(q.pop(0))
            else:return
    
            
        

B=BST()
root=0
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
   root=B.insert(root,i)
B.printTree(root)
print('inorder : ',end='')
B.inorder(root)
print()
print('preorder : ',end='')
B.preorder(root)
print()
print('postorder : ',end='')
B.postorder(root)
print()
print('bfs : ',end='')
B.BFS(root)

                