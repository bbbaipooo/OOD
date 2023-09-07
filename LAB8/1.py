class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        
class BinarySearchTree():
    def __init__(self):
        self.root=None
        
    def printTree(self,node,level=0):
        if node!=None:
            self.printTree(node.right,level+1)
            print('     '*level,node.data)
            self.printTree(node.left,level+1)
            
    def insert(self,data):
        node=Node(data)
        if self.root==None:
            self.root=node
            print('*')
        else:
            r=self.root
            while True:
                if r.data>data:
                    if r.left==None:
                        r.left=node
                        print('L*')
                        break
                    else:
                        r=r.left
                        print('L',end='')
                else:
                    if r.right==None:
                        r.right=node
                        print('R*')
                        break
                    else:
                        r=r.right
                        print('R',end='')
 
                        
tree=BinarySearchTree()
inp=list(map(int,input('Enter Input : ').split()))
for i in inp:
    tree.insert(i)
        