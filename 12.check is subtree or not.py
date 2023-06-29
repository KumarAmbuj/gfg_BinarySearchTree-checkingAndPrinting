class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def checkwhole(node1,node2):
    if node1==None and node2==None:
        return True
    if node1 and node2:
        return (node1.val == node2.val) and checkwhole(node1.left, node2.left) and checkwhole(node1.right, node2.right)
    return False
def checkrec(node,node1):
    if node==None:
        return False

    if node.val==node1.val:
        if checkwhole(node,node1):
            return True
        else:
            return False

    if checkrec(node.left,node1):
        return True
    if checkrec(node.right,node1):
        return True

    return False



def check(node1,node2):
    print(checkrec(node1,node2))



T = Node('a');
T.left = Node('b');
T.right = Node('d');
T.left.left = Node('c');
T.right.right = Node('e');


S = Node('a');
S.left = Node('b');
S.right = Node('d');
S.left.left = Node('c');

check(T,S)


T = Node('a');
T.left = Node('b');
T.right = Node('d');
T.left.left = Node('c');
T.right.right = Node('e');


S = Node('b');

S.left = Node('c');

check(T,S)
