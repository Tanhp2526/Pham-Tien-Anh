#compare theo vong lap
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
            while current.next != None:
                current = current.next
            current.next = node
    
    def compare_list(self, head1):
        current1 = self.head
        current2 = head1

        while current1 and current2:
            if current1.data != current2.data:
                return 0
            current1 = current1.next
            current2 = current2.next

        if current1 is None and current2 is None:
            return 1 
        
        return 0

n = int(input())

for t in range(n):
    cnt1 = int(input())
    llist1 = LinkedList()

    for i in range(cnt1):
        node1 = int(input())
        llist1.insert_node(node1)
    
    cnt2 = int(input())
    llist2 = LinkedList()
    for i in range(cnt2):
        node2 = int(input())
        llist2.insert_node(node2)

    res = llist1.compare_list(llist2.head)
    print(res)    

    
    