class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #def __str__(self):
    #    return str(self.data)


class BST:
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
            print('     ' * level, node.data)#######
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
