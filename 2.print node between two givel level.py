class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def printnode(node,low,high,hash,l):

    if node==None:
        return

    if l>high:
        return

    if l>=low and l<=high:
        if l not in hash:
            hash[l] = []
            hash[l].append(node.val)
        else:
            hash[l].append(node.val)
    printnode(node.left,low,high,hash,l+1)
    printnode(node.right,low,high,hash,l+1)


def check(node,low,high):
    hash={}
    printnode(node,low,high,hash,1)

    for x in hash:
        for z in hash[x]:
            print(z,end=' ')
        print()

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
check(root,2,4)