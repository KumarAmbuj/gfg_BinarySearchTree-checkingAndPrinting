class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def storevertical(node,d,hash):
    if node==None:
        return
    if d not in hash:
        hash[d]=[]
        hash[d].append(node.val)
    else:
        hash[d].append(node.val)

    storevertical(node.left,d-1,hash)
    storevertical(node.right,d+1,hash)
def Partition(arr,p,r):
    i=p-1
    x=arr[r]
    for j in range(p,r):
        if arr[j]<x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def Quicksort(arr,p,r):
    if p<r:
        q=Partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)

def verticalorder(node):
    hash={}
    storevertical(node,0,hash)

    arr=[]
    for x in hash:
        arr.append(x)
    Quicksort(arr,0,len(arr)-1)

    for x in arr:

        l=hash[x]

        for z in l:
            print(z,end=' ')
        print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.left = Node(10)
root.right.right.right = Node(9)
root.right.right.left.right = Node(11)
root.right.right.left.right.right = Node(12)
verticalorder(root)