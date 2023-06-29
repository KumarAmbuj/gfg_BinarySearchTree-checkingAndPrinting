class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Pair:
    def __init__(self,flag=False,h=-1):
        self.falg=flag
        self.h=h
def check(node):

    if node==None:
        np=Pair()
        np.flag=True
        return np

    lp=check(node.left)
    rp=check(node.right)

    np=Pair()
    h=lp.h-rp.h
    np.flag=(h==1 or h==0)and lp.flag and rp.flag

    np.h=max(lp.h,rp.h)+1

    return np

def complete(node):
    np=check(node)
    print(np.flag)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
complete(root)

