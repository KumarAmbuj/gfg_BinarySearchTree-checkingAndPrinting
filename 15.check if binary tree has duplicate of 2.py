class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Pair():
    def __init__(self,size=0,s=''):

        self.size=size
        self.s=s

def check(node,hash):

    global res

    if node==None:
        np=Pair()

        np.size=0
        np.s=''
        return np

    lp=check(node.left,hash)
    rp=check(node.right,hash)

    np=Pair()

    s=node.val+lp.s+rp.s
    size=lp.size+rp.size+1

    if s in hash and hash[s]==size and size>=2:
        res=True
    else:
        hash[s]=size

    np.s=s
    np.size=size
    return np

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('B')
root.right.right.right = Node('E')
root.right.right.left= Node('D')
res=False
hash={}
n=check(root,hash)
print(res)






