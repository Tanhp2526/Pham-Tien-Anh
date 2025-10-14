class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #them node vao cuoi danh sach
    def append(self,data):
        node = Node(data)# khoi tao 1 node
        if not self.head: # neu nhu danh sach rong
            self.head = node
            return 
        
        current = self.head
        while current.next != None : # duyet tung node đen khi gap None
            current = current.next
        current.next = node # them node moi vao sau node cuoi

    def print(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print()

