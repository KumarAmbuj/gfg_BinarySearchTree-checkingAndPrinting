class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def check(node,c,l):
    if node==None:
        return False

    if node.left==None and node.right==None:
        if c[0]==-1:
            c[0]=l

            return True
        else:


            return c[0]==l


    return (node.left!=None and node.right!=None) and check(node.left,c,l+1) and check(node.right,c,l+1)

def checkperfect(node,):
    c=[-1]
    print(check(node,c,0))


root = Node(10)
root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)


checkperfect(root)