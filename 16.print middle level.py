class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def checkrec(node,c,l):
    if node.left==None and node.right==None:
        if c[0]==-1:
            c[0]=l
        return

    checkrec(node.left,c,l+1)
    checkrec(node.right,c,l+1)

    if l==c[0]//2:
        print(node.val)

def check(node):

    c=[-1]

    checkrec(node,c,0)


n1 = Node(1);
n2 = Node(2);
n3 = Node(3);
n4 = Node(4);
n5 = Node(5);
n6 = Node(6);
n7 = Node(7);

n2.left = n4;
n2.right = n5;
n3.left = n6;
n3.right = n7;
n1.left = n2;
n1.right = n3;

check(n1)