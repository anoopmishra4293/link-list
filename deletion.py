class Node:

    def __init__(self,val):
        self.val = val
        self.next = None

def printll(head):
    ptr = head
    while ptr:
        print(ptr.val, "->", end = " ")
        ptr = ptr.next
    print("null")


def deletion_front(head):
    if not head:
        return head
    a=head
    head=head.next
    del a
    return head


def deletion_rear(head):
    if not head:
        return head
    ptr=head
    while ptr and ptr.next!=None:
        prev=ptr
        ptr=ptr.next
    if ptr.next== None:
        prev.next=None
        del ptr
        return head


def deletion_val(head,x):
    if not head:
        return head
    ptr=head

    if  head.val==x:
        b=head.val
        head=head.next
        del b
        return head

    while ptr and ptr.val!=x:
        prev=ptr
        ptr=ptr.next
    if ptr.val==x:
        prev.next=ptr.next
        del ptr
    return head


n1 = Node(5)
n1.next = Node(4)
n1.next.next = Node(6)
n1.next.next.next = Node(2)
n1.next.next.next.next = Node(8)
n1.next.next.next.next.next = Node(52)
n1.next.next.next.next.next.next = Node(68)

head=n1

print("Before deliting nodes: ")
printll(head)


head = deletion_front(head)
head = deletion_rear(head)
head = deletion_val(head,52)
printll(head)