class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def fullnode(node):
    if node==None:
        return True

    if node.left==None and node.right==None:
        return True
    return (node.left!=None and node.right!=None) and fullnode(node.left) and fullnode(node.right)

def check(node):

    print(fullnode(node))


root = Node(10);
root.left = Node(20);
root.right = Node(30);

root.left.right = Node(40);
root.left.left = Node(50);
root.right.left = Node(60);
root.right.right = Node(70);

root.left.left.left = Node(80);
root.left.left.right = Node(90);
root.left.right.left = Node(80);
root.left.right.right = Node(90);
root.right.left.left = Node(80);
root.right.left.right = Node(90);
root.right.right.left = Node(80);
root.right.right.right = Node(90);
check(root)