class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def printnode(node,l,d):
    if node==None:
        return

    if d not in l:
        print(node.val,end=' ')
        l.append(d)

    printnode(node.right,l,d+1)
    printnode(node.left,l,d+1)

def rightview(node):
    l=[]
    printnode(node,l,0)

root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)
rightview(root)
print()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

rightview(root)