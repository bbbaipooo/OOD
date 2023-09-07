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

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def checkpos(self,data):
        run=self.root
        if run.data==data:
            return 'Root'
        else:
            while True:
                if run.data>data:
                    run=run.left
                else:
                    run=run.right
                
                if run.data==data and not run.left and not run.right:
                    return 'Leaf'
                elif run.data==data:
                    return 'Inner'
                elif not run.left and not run.right:
                    return 'Not exist'
                
                    
T = BinarySearchTree()
inp =list(map(int,input('Enter Input : ').split()))
for i in inp[1::]:
    root = T.insert(i)
T.printTree(root)
print(T.checkpos(inp[0]))
