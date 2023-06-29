class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def Queue():
    queue=[]
    return queue

def Enqueue(q,s):
    q.append(s)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

def sortedlevel(node):
    queue=Queue()
    Enqueue(queue,node)
    Enqueue(queue,None)
    l=[]

    print(node.val)
    while(Size(queue)>1):
        rem=Dequeue(queue)

        if rem==None:
            x=l[::-1]
            for z in x:
                print(z,end=' ')
            print()

            l=[]
            Enqueue(queue,None)

        else:
            if rem.left:
                Enqueue(queue,rem.left)
                l.append(rem.left.val)
            if rem.right:
                Enqueue(queue,rem.right)
                l.append(rem.right.val)


root = Node(7)
root.left = Node(6)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(3)
root.right.left = Node(2)
root.right.right = Node(1)
sortedlevel(root)

