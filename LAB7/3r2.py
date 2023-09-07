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
                        
    def change(self,root,data):
        if root:
            self.change(root.right,data)
            if root.data>data:
                root.data = root.data*3
            self.change(root.left,data)
            
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
T.change(root,int(inp[1]))
T.printTree(root)