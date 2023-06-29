class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Pair:
    def __init__(self,flag=False,val=0):
        self.flag=flag
        self.val=val


def checksum(node):

    if node==None:
        np=Pair(True,0)
        return np
    if node.left==None and node.right==None:
        np=Pair(True,node.val)
        return np

    lp=checksum(node.left)
    rp=checksum(node.right)

    np=Pair()
    np.flag=(lp.val+rp.val==node.val)and(lp.flag)and(rp.flag)
    np.val=node.val

    return np



def check(node):

    print(checksum(node).flag)

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(2)
check(root)