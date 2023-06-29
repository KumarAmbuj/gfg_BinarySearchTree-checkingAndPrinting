class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Pair():
    def __init__(self,h=0,dia=0,s=''):
        self.h=h
        self.dia=dia


def check(node):

    if node==None:
        np=Pair(-1,0)
        return np
    if node.left==None and node.right==None:
        np = Pair(0, 0)
        return np


    lp=check(node.left)
    rp=check(node.right)

    np=Pair()

    dia=lp.h+rp.h+2
    np.dia=max(dia,lp.dia,rp.dia)
    np.h=max(lp.h,rp.h)+1

    return np


def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=' ')
        inorder(node.right)


def printleaftoleaf(node):
   print(check(node).dia)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.left.left.right = Node(8)
root.left.left.right.left = Node(9)
root.left.right.left.left = Node(10)
printleaftoleaf(root)
