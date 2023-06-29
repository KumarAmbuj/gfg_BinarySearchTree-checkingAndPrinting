class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def printknode(node,block,k,s):
    if node==None:
        return
    if k<0:
        return

    if node==block:
        return

    if k==0:
        if node.left!=None and node.right!=None:
            s.add(node.val)

    printknode(node.left,block,k-1,s)
    printknode(node.right,block,k-1,s)

def printkdist(arr,k,s):

    for i in range(len(arr)):
        block=None
        if i>0:
            block=arr[i-1]
        printknode(arr[i],block,k-i,s)

def storeleaf(node,arr,k,s):
    if node==None:
        return

    if node.left==None and node.right==None:
        arr.append(node)
        l=arr[::-1]
        printkdist(l,k,s)
        arr.pop()
        return

    arr.append(node)

    storeleaf(node.left,arr,k,s)
    storeleaf(node.right,arr,k,s)
    arr.pop()


def kdist(node,k):
    arr=[]
    s=set()

    storeleaf(node,arr,k,s)

    for x in s:
        print(x,end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
kdist(root,2)