class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def count(head):
    if not head:
        return None
    
    ptr = head
    count=0
    while ptr:
        ptr=ptr.next
        count += 1
    return count


n1 = Node(5)
n1.next = Node(4)
n1.next.next = Node(6)
n1.next.next.next = Node(2)
n1.next.next.next.next = Node(8)
n1.next.next.next.next.next = Node(52)
n1.next.next.next.next.next.next = Node(68)

head=n1

print("count=",count(head))