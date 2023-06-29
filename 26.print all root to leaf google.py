class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def printarray(arr):
    mn=99
    for i in range(len(arr)):
        mn=min(mn,arr[i][1])

    for i in range(len(arr)):
        x=abs(abs(mn)-abs(arr[i][1]))

        for j in range(x):
            print('-',end='')
        print(arr[i][0])
    print('==========')



def check(node,d,l):

    if node==None:
        return
    if node.left==None and node.right==None:
        l.append([node.val,d])
        printarray(l)
        l.pop()
        return

    l.append([node.val,d])


    check(node.left,d-1,l)
    check(node.right,d+1,l)

    l.pop()

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')
l=[]
check(root,0,l)

