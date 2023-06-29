class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def checksum(node):
    if node==None:
        return 1
    if node.left==None and node.right==None:
        return 1

    l=0
    r=0

    if node.left:
        l=node.left.val

    if node.right:
        r=node.right.val

    if (node.val==l+r) and checksum(node.left) and checksum(node.right):

        return 1
    else:
        return 0

def check(node):

    print(checksum(node))

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(2)
check(root)