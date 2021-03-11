class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

n1 = Node(5)
n1.next = Node(4)
n1.next.next = Node(6)
n1.next.next.next = Node(2)
n1.next.next.next.next = Node(8)

head = n1
ptr = head

print(ptr!=None)
while ptr:
    print(ptr.val,"->",end=" ")
    ptr=ptr.next

print("null")