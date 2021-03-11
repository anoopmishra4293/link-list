class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def printll(head):
    ptr=head
    while ptr:
        print(ptr.val,"->",end=" ")
        ptr=ptr.next
    print("null")


def insert_front(head,val):
    n = Node(val)
    if not head:
        head=n
        return head
    n.next=head
    head=n
    return head


def insert_rear(head,val):
    n=Node(val)
    if not head:
        head=n
        return head
    ptr = head
    while ptr and ptr.next!=None:
        ptr = ptr.next
    if ptr.next == None:
        ptr.next = n
        n.next = None
        return head
    

def insert_before(head,x,val):
    n = Node(val)
    if not head:
        return head
    ptr=head
    while ptr and ptr.val!=x:
        prev=ptr
        ptr=ptr.next
    if not ptr:
        return head
    n.next = ptr
    prev.next = n
    return head


def insert_after(head,x,val):
    n = Node(val)
    if not head:
        return head
    ptr=head
    while ptr and ptr.val!=x:
        ptr=ptr.next
    if not ptr:
        return head
    n.next=ptr.next
    ptr.next=n
    return head


head=None
head = insert_front(head,1)
head = insert_front(head,2)
head = insert_front(head,3)
head = insert_after(head,2,4)
head = insert_rear(head,5)
head = insert_rear(head,6)
head = insert_before(head,5,7)
head = insert_before(head,6,8)
printll(head)