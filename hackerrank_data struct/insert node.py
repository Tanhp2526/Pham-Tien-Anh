#chen vào cuoi
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def insert_node(head, data):
    node = Node(data)

    if not head:
        return node
    
    else :
        current = head
        while current.next != None:
            current = current.next
        current.next = node

    
    return head

def print_list(head):
    current = head 
    while current:
        print(current.data)
        current = current.next
n = int(input())
list = LinkedList()

for i in range(n):
    node = int(input())
    list_head = insert_node(list.head, node)
    list.head = list_head


print_list(list.head)