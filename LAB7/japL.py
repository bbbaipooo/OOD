class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None

    def insert(self,node, data):
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
            return node #ชี้กลับ ex.node.right=insert() ==กลายเป็นชี้Noneเมื่อมีการต่อnodeลงไปอีก
        
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)#######
            self.printTree(node.left, level + 1)
            
            
t=BST()
root=None
inp=input('Enter input : ').split()
for i in inp:
    root=t.insert(root,i)
t.printTree(root)
            
        