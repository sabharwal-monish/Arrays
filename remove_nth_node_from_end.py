class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def remove_nth_node_from_end(head, n):
    dummy = Node(-1)
    dummy = head.next
    slow=fast=head

    for i in range(n):
        if fast.next is None:
            return head
    fast=fast.next

    while fast.next is not None:
        fast=fast.next
        slow=slow.next
    slow.next = slow.next.next

    return head

def print_list(head):
    curr=head
    while curr is not None:
        print(curr.data, end="->")
        curr=curr.next
    print('None')

#Driver Code
head=Node(8)
head.next=Node(7)
head.next.next=Node(6)
head.next.next.next=Node(4)
n=3

head=remove_nth_node_from_end(head,n)
print_list(head)

