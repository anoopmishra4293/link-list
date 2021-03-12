class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def printll(head):
    ptr = head
    while ptr:
        print(ptr.val, "->", end=" ")
        ptr = ptr.next
    print("null")

def deletion_link_list(head):
    if not head:
        return None
    ptr=head
    while ptr:
        a = ptr
        ptr = ptr.next
        del a

n1 = Node(5)
n1.next = Node(4)
n1.next.next = Node(6)
n1.next.next.next = Node(2)
n1.next.next.next.next = Node(8)
n1.next.next.next.next.next = Node(52)
n1.next.next.next.next.next.next = Node(68)

head=n1

printll(head)

print(deletion_link_list(head))