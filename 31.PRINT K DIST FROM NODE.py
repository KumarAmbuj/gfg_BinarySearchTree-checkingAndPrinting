class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def allkdist(node,node1,l):

    if node==None:
        return False

    if node==node1:
        l.append(node)
        return True

    if allkdist(node.left,node1,l):
        l.append(node)
        return True
    if allkdist(node.right,node1,l):
        l.append(node)

        return True
    return False
def printknode(node,block,k):
    if node==None:
        return

    if k<0:
        return

    if node==block:
        return

    if k==0:
        print(node.val,end=' ')
    printknode(node.left,block,k-1)
    printknode(node.right,block,k-1)

def printkdist(node,k,node1):

    arr=[]
    allkdist(node,node1,arr)




    for i in range(len(arr)):
        block=None
        if i>0:
            block=arr[i-1]
        printknode(arr[i],block,k-i)

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target = root.left.right
printkdist(root,2,target)



