class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            r = self.root
            while True:
                if r.data > data:
                    if r.left == None:
                        r.left = node
                        return self.root
                    else:
                        r = r.left
                else:
                    if r.right == None:
                        r.right = node
                        return self.root
                    else:
                        r = r.right
                        
    def checkMul3(self,node,k,level=0):
        if node != None:
            self.checkMul3(node.right,k, level + 1)
            if node.data>k:
                print('     ' * level, node.data*3)
            else:
                print('     ' * level, node)
            self.checkMul3(node.left,k, level + 1)
    
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BinarySearchTree()
inp = input('Enter Input : ').split('/')
inp0=list(map(int,inp[0].split()))
for i in inp0:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
T.checkMul3(root,int(inp[1]))
