#them vao vi tri dac biet
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
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
    
    def append(self, data, position):
        new_node = Node(data)

        if position == 0 :
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head 
        index = 0
        while current != None and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            return
        
        new_node.next = current.next
        current.next = new_node

n = int(input())
llsit = LinkedList()

for i in range(n):
    node = int(input())
    llsit.insert_node(node)

data = int(input())
position = int(input())
llsit.append(data, position)
llsit.display()
