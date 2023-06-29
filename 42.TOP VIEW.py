class Node:
    def __init__(self,val,d=0):
        self.val=val
        self.left=None
        self.right=None
        self.d=d
def Queue():
    queue=[]
    return queue
def Enqueue(q,x):
    q.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(queue):
    return len(queue)



def Topview(node):
    l=[]
    queue=Queue()

    Enqueue(queue,node)
    while(Size(queue)):
        rem=Dequeue(queue)

        if rem.d not in l:
            print(rem.val)
            l.append(rem.d)

        if rem.left:
            Enqueue(queue,rem.left)
            rem.left.d=rem.d-1
        if rem.right:
            Enqueue(queue,rem.right)
            rem.right.d=rem.d+1






root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
Topview(root)