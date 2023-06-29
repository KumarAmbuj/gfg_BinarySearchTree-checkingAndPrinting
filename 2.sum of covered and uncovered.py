class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def uncoverright(node):
    if node.left == None and node.right == None:
        return node.val

    if node.right:
        return node.val + uncoverright(node.right)
    else:
        return node.val + uncoverright(node.left)
def uncoverleft(node):
    if node.left==None and node.right==None:
        return node.val

    if node.left:
        return node.val+uncoverleft(node.left)
    else:
        return node.val+uncoverleft(node.right)


def Sum(node):
    if node==None:
        return 0
    if node.left==None and node.right==None:
        return node.val

    return node.val+Sum(node.left)+Sum(node.right)


def check(root):

    uncover=uncoverleft(root.left)+uncoverright(root.right)+root.val
    cover=Sum(root)-uncover

    print(cover==uncover)


root = Node(8)
root.left = Node(3)

root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

root.right = Node(10)
root.right.right = Node(14)
root.right.right.left = Node(13)
check(root)

