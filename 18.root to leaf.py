class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def check(node,s):
    if node==None:
        return

    if node.left==None and node.right==None:
        if len(s)>0:
            s=s+'->'+str(node.val)
        elif len(s)==0:
            s=s+str(node.val)
        print(s)
        return
    if len(s)==0:
        s=s+str(node.val)
    else:
        s = s + '->' + str(node.val)

    check(node.left,s)
    check(node.right,s)

def printleaf(node):

    check(node,'')

root = Node(1);
root.left = Node(2);
root.right = Node(3);
root.left.left = Node(4);
root.left.right = Node(5);
printleaf(root)




