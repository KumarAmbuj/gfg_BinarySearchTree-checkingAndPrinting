class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def roottonode(node,arr,x):

    if node==None:
        return False

    arr.append(node.val)

    if node.val==x:
        return True


    if roottonode(node.left,arr,x) or roottonode(node.right,arr,x):
        return True
    arr.pop()
    return False
def check(node,x):
    arr=[]
    roottonode(node,arr,x)
    print(arr)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
check(root,5)



