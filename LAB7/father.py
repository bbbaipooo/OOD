class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def __str__(self):
        return str(self.data)
    
class BinarySearchTree():
    def __init__(self):
        self.root=None
        
    def insert(self,data):
        node=Node(data)
        if self.root==None:
            self.root=node
        else:
            run=self.root
            while True:
                if run.data>data:
                    if run.left==None:
                        run.left=node
                        break
                    else:
                        run=run.left
                else:
                    if run.right==None:
                        run.right=node
                        break
                    else:
                        run=run.right
                        
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
def father(root,k):
    run=root
    if run.data==k:
        return f'None Because {k} is Root'
    else:
        while True:
            if not run.left and not run.right:
                return 'not found'
            if run.data>k and run.left.data==k:
                return run.data
            elif run.data<k and run.right.data==k:
                return run.data
            if run.data>k:
                run=run.left
            elif run.data<k:
                run=run.right
    
            
tree=BinarySearchTree()
inp=input('Enter Input : ').split('/')
inp0=list(map(int,inp[0].split()))
for i in inp0:
    tree.insert(i)
tree.printTree(tree.root)
print(father(tree.root,int(inp[1])))