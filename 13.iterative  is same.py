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
def check(node1,node2):

    queue1=Queue()
    queue2=Queue()

    Enqueue(queue1,node1)
    Enqueue(queue2,node2)

    while(Size(queue1) and Size(queue2)):

        rem1=Dequeue(queue1)
        rem2=Dequeue(queue2)

        if rem1 and rem2:
            if rem1.val!=rem2.val:
                return False
            if rem1.left:
                Enqueue(queue1,rem1.left)

                Enqueue(queue2,rem2.left)
            if rem1.right:
                Enqueue(queue1,rem1.right)

                Enqueue(queue2,rem2.right)
        else:
            return False
    return True


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

print(check(root1,root2))



