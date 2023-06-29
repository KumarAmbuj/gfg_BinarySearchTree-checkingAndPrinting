class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def cousin(node,parent,hash,l):
    if node==None:
        return

    hash[node.val]=(l,parent)
    cousin(node.left,node,hash,l+1)
    cousin(node.right,node,hash,l+1)



def printcousin(node,node1):
    hash={}

    cousin(node,None,hash,0)

    level=hash[node1.val][0]
    parent=hash[node1.val][1]

    for x in hash:

        if hash[x][0]==level and hash[x][1]!=parent:
            print(x)





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
printcousin(root,root.left.right)