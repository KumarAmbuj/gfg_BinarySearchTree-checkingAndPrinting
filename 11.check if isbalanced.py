class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Pair():
    def __init__(self,flag=False,h=-1):
        self.flag=flag
        self.h=h
def isbalance(node):
    if node == None:
        np = Pair()
        np.flag = True
        np.h = 0
        return np




    lp=isbalance(node.left)
    rp=isbalance(node.right)

    np=Pair()

    mx=max(lp.h,rp.h)+1
    mn=min(lp.h,rp.h)+1
    np.flag=(mx<=2*mn) and lp.flag and rp.flag
    np.h=mx
    return np




def check(node):
    np=isbalance(node)
    print(np.flag)


root = Node(10)
root.left = Node(5)
root.right = Node(100)
root.right.left = Node(50)
root.right.right = Node(150)
root.right.left.left = Node(40)
check(root)

root = Node(10)
root.right = Node(100)
root.right.right = Node(150)
check(root)