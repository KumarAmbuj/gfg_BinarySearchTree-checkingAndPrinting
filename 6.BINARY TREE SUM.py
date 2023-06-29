class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Pair:
    def __init__(self,val=0,flag=True):
        self.val=val
        self.flag=flag

def checkrec(node):

    if node==None:
        np=Pair()
        np.val=0
        np.flag=True
        return np
    if node.left==None and node.right==None:
        np=Pair()
        np.val=node.val
        np.flag=True
        return np

    lp=checkrec(node.left)
    rp=checkrec(node.right)

    np=Pair()
    np.flag=(node.val==lp.val+rp.val) and lp.flag and rp.flag
    np.val=lp.val+rp.val+node.val

    return np



def check(node):
    mp=checkrec(node)
    print(mp.flag)

root = Node(26)
root.left= Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)
check(root)

