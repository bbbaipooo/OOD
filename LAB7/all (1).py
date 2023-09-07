class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root ,data):
        if not root:
            return Node(data)
        if root:
            if data < root.data:
                root.left = self.insert(root.left,data)
            else:
                root.right = self.insert(root.right,data)
        return root
    def checkpos(self,k):
        t = root 
        while True:
            if (k==t.data):
                if k==root.data:
                    print('Root')
                    return
                elif t.left ==None and t.right ==None:
                    print('Leaf')
                    return
                else:
                    print('Inner')
                    return
            elif(k<t.data):
                if t.left ==None:
                    print('Not exits')
                    return
                else:t=t.left
            else:
                if t.right ==None:
                    print('Not exits')
                    return
                else:t=t.right
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def below(self,node,data):
        global summ
        if node !=None:
            if node.data<=data:
                print(node.data,end=' ')
            self.below(node.right,data)
            self.below(node.left,data)
        return summ
    def delete(self,root, data):
        if root is None:
            print("Error! Not Found DATA")
            return None
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is not None and root.right is not None: 
                cur = root.right
                while cur.left is not None:
                    cur = cur.left
                root.data, cur.data = cur.data, root.data
                root.right = self.delete(root.right, data)
            elif root.left is not None:
                return root.left
            elif root.right is not None:
                return root.right
            else:
                return None
        return root
    def printPre(self, node):
        if node != None:
            print(node,end=' ')
            self.printPre(node.left)
            self.printPre(node.right)
    def printIn(self, node):
        if node != None:
            self.printIn(node.left)
            print(node,end=' ')
            self.printIn(node.right)
    def printPost(self, node):
        if node != None:
            self.printPost(node.left)
            self.printPost(node.right)
            print(node,end=' ')
    def printBreadth(self,node,q=[]):
        if node !=None:
            print(node,end=' ')
        if node.left!=None:q.append(node.left)
        if node.right!=None:q.append(node.right)
        if len(q)!=0:self.printBreadth(q.pop(0),q)
        else:return
    def Height(self,node):
            if node !=None:
                return max(self.Height(node.left),self.Height(node.right))+1
            else: return -1   
    def lessThan(self,node,data):
        global summ
        if node !=None:
            if node.data<=data:
                summ+=1
            self.lessThan(node.right,data)
            self.lessThan(node.left,data)
        return summ    
    def printMin(self,node):
        if node.left!=None:
            self.printMin(node.left)
        else:return print(node)
    def printMax(self,node):
        if node.right!=None:
            self.printMax(node.right)
        else:return print(node)
    def MoreThan(self,node,data):
        global summ
        if node !=None:
            if node.data>=data:
                summ+=1
            self.MoreThan(node.right,data)
            self.MoreThan(node.left,data)
        return summ
def father(r,data):
    if r == None:
        return 'Not Found data'
    if r.data == data:
        return (f'None Because {data} is Root')
    c = r 
    while c !=None and (c.left !=None or c.right !=None):
        if c.left !=None:
            node = c.left
            if node.data == data:
                return c.data
        if c.right !=None:
            node = c.right
            if node.data ==data:
                return c.data
        if data <= c.data:
            c= c.left
        else:
            c= c.right
    return "Not Found Data"

B=BST()

