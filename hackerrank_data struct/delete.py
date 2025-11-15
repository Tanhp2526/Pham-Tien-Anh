#xoa theo gia tri node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
    
    def delete_node(self, key):
        current = self.head
        prev = None 

        if current != None and current.data == key:
            self.head = current.next
            return
        
        while current != None and current.data != key:
            prev = current 
            current = current.next 

        if current is None:
            return
        
        prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next 
        print(None)

n = int(input())
llist = LinkedList()

for i in range(n):
    new_node = int(input())
    llist.insert_node(new_node)

value = int(input())
llist.delete_node(value)
llist.display()


