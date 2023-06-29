class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def storenode(node,hash,d):
    if node==None:
        return

    if d not in hash:
        hash[d]=node.val

    storenode(node.left,hash,d-1)
    storenode(node.right,hash,d+1)



def lrnode(node):
    hash={}
    storenode(node,hash,0)

    

    arr=[]
    for x in hash:
        arr.append(x)
    arr.sort()

    for x in arr:
        print(hash[x],end=' ')

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
lrnode(root)