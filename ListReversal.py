def __init__(self, data):
    self.next = None
    self.data = data

def listReversal(head):
    curr = head
    prev = None

    while curr is not None:
        temp = curr.next

        curr.next = prev

        prev = curr
        curr = temp
    return prev

def printList(node):
    while node is not None:
        print(f" {node.data}", end="")
        node = node.next
    print()

if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Given Linked list:", end="")
    printList(head)

    head = reverseList(head)

    print("Reversed Linked List:", end="")
    printList(head)