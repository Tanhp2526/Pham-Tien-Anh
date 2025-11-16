class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
    
    def reverse_list(self):
        current = self.head
        prev = None

        while current:
            tx = current.next
            current.next = prev
            prev = current
            current = tx

        self.head = prev
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

n = int(input())

for t in range(n):
    cnt = int(input())
    llist = LinkedList()

    for i in range(cnt):
        node = int(input())
        llist.insert_node(node)

    llist.reverse_list()
    llist.display()

