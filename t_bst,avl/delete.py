class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level+1)
            print("    "*level, node.data)
            self.printTree(node.left, level+1)

    def insert(self, node, data):
        if self.root == None:
            self.root = TreeNode(data)
            return self.root
        else:
            if node != None:
                if data < node.data:
                    node.left = self.insert(node.left, data)
                else:
                    node.right = self.insert(node.right, data)
            else:
                return TreeNode(data)
            return node

    def delete(self,node,data):
        if node==None:
            print('Error')
            return
        else:
            if node.data>data:
                node.left=self.delete(node.left,data)
            elif node.data<data:
                node.right=self.delete(node.right,data)
            else:
                if node.left and node.right:
                    cur=node.right
                    while cur.left:
                        cur=cur.left
                    node.data,cur.data=cur.data,node.data
                    node.right=self.delete(node.right,data)
                elif node.left:
                    return node.left
                elif node.right:
                    return node.right
                else:
                    return None
            return node
  
            

t = BST()
root = None
inp1, inp2 = input('Enter Input : ').split('/')
inp1 = list(map(int, inp1.split()))
inp2 = int(inp2)
for i in inp1: 
    root = t.insert(root, i)
t.printTree(root)
t.delete(root, inp2)
print('===')
t.printTree(root)
