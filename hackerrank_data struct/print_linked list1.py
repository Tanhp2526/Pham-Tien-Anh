class Node:
    def __init__(self, data):
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
            while current.next != None :
                current = current.next

            current.next = node

    
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

n = int(input())

linkedlisst = LinkedList()

for i in range(n):
    node = int(input())
    linkedlisst.insert_node(node)

linkedlisst.print()
        
        
         
        

        

