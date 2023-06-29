class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Pair:
    def __init__(self,flag=False,level=-1):
        self.flag=flag
        self.level=level
def height(root,node,l,level):
    if root==None:
        return False

    if root==node:
        l[0]=level
        return True

    if height(root.left,node,l,level+1):
        return True

    if height(root.right,node,l,level+1):
        return True
    return False

def sibling(node,a,b):
    if node==None:
        return False

    return ((node.left==a and node.right==b)or(node.left==b and node.right==a)) or sibling(node.left,a,b) or sibling(node.right,a,b)


def isCousin(root,node1,node2):
    l=[-1]
    a=height(root,node1,l,0)

    c = [-1]
    b=height(root, node2, c, 0)

    if a and b:
        flag= l[0]==c[0] and not sibling(root,node1,node2)
        print(flag)
    else:
        print(False)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

node1 = root.right
node2 = root.right.right
isCousin(root,node1,node2)



