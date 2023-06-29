class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def printk(node,k):

    if node==None:
        return
    if k<0:
        return

    if k==0:
        print(node.val,end=' ')

    printk(node.left,k-1)
    printk(node.right,k-1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(8)
printk(root,2)
