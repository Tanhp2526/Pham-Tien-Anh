class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def insert_node(llist, data):
    node = Node(data)
    node.next = llist

    return node
def print_list(head):
    current = head
    while current:
        print(current.data)
        current = current.next
n = int(input())
llist = LinkedList()

for i in range(n):
    data = int(input())
    llist_head = insert_node(llist.head, data)
    llist.head = llist_head

print_list(llist.head)


