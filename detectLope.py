
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def detectLoop(head):
    st = set()

    while head is not None:

        # If this node is already present
        # in hashmap it means there is a cycle
        if head in st:
            return True

        # If we are seeing the node for
        # the first time, insert it in hash
        st.add(head)

        head = head.next

    return False

if __name__ ==  '__main__':
    head = Node(5)
    head.next = Node(6)
    head.next.next = Node(8)
    head.next.next.next = head.next

    if detectLoop(head):
        print(True)
    else:
        print(False)