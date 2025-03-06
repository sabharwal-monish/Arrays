class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def sortedMerge(head1, head2):
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data <= head2.data:
        head1.next = sortedMerge(head1.next, head2)
        return head1

    else:
        head2.next = sortedMerge(head2.next, head1)
        return head2

def printList(cur):

    while cur is not None:
        print(cur.data, end=" ")
        cur=cur.next


if __name__ == "__main__":
    # First linked list: 5 -> 10 -> 15
    head1 = Node(5)
    head1.next = Node(10)
    head1.next.next = Node(15)

    # Second linked list: 2 -> 3 -> 20
    head2 = Node(2)
    head2.next = Node(3)
    head2.next.next = Node(20)

    res = sortedMerge(head1, head2)
    printList(res)