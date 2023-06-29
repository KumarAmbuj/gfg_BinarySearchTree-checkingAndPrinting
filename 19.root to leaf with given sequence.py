class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def checkrec(node,arr,i,n):
    if node==None:
        return False

    if node.left==None and node.right==None:
        if arr[i]==node.val and i==n-1:
            return True

    return (node.val==arr[i]) and (checkrec(node.left,arr,i+1,n) or checkrec(node.right,arr,i+1,n))

def check(node,arr):

    print(checkrec(node,arr,0,len(arr)))

arr = [5, 8, 6, 7]
n = len(arr)
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(1)
root.right.left = Node(6)
root.right.left.right = Node(7)
check(root,arr)