class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


n1 = Node(5)
n2 = Node(6)
n3 = Node(8)

n1.next=n2
n2.next=n3

print(n1.val,"->",n1.next.val,"->",n1.next.next.val)
print(n1.val,"->",n2.val,"->",n3.val)

head= n1
print(head.val,"->",head.next.val,"->",head.next.next.val)