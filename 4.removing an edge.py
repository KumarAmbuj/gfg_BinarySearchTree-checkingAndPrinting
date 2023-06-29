class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def count(node):
    if node==None:
        return 0

    return count(node.left)+count(node.right)+1
def checkrec(node,n):
    global res

    if node==None:
        return 0

    c=checkrec(node.left,n)+checkrec(node.right,n)+1

    if c==n-c:
        res=True
    return c

def check(root):
    n=count(root)

    checkrec(root,n)
    print(res)


res = False
root = Node(5)
root.left = Node(1)
root.right = Node(6)
root.left.left = Node(3)
root.right.left = Node(7)
root.right.right = Node(4)

check(root)