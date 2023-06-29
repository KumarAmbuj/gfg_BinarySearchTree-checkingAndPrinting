class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def checklevel(node,l,level):
    if node==None:
        return True

    if node.left==None and node.right==None:
        if l[0]==-1:
            l[0]=level
            return True
        else:
            return l[0]==level

    return checklevel(node.left,l,level+1) and checklevel(node.right,l,level+1)

def check(node):
    l=[-1]
    print(checklevel(node,l,0))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.right = Node(9)
check(root)
