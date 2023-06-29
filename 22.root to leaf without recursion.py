class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def Stack():
    s=[]
    return s
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)
def Peek(s):
    return s[-1]

class Pair():
    def __init__(self,node,s,l):
        self.node=node
        self.s=s
        self.l=l


def roottoleaf(node):
    l=[]
    l.append(node.val)
    p=Pair(node,1,l)
    stack=Stack()
    Push(stack,p)

    while(Size(stack)):

        top=Peek(stack)

        if top.s==1:
            top.s+=1
            if top.node.left:
                l=top.l.copy()
                l.append(top.node.left.val)
                np=Pair(top.node.left,1,l)
                Push(stack,np)

        elif top.s==2:
            top.s += 1
            if top.node.right:
                l = top.l.copy()
                l.append(top.node.right.val)
                np = Pair(top.node.right, 1, l)
                Push(stack, np)

        elif top.s==3:
            x=Pop(stack)
            if x.node.left==None and x.node.right==None:
                print(x.l)

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

roottoleaf(root)



