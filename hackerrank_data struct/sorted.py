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
    
    def merge_list(self, head1):
        dummy = Node(-1)
        tail = dummy

        current1 = self.head
        current2 = head1

        while current1 and current2:
            if current1.data <= current2.data:
                tail.next = current1
                tail = tail.next
                current1 = current1.next
            else:
                tail.next = current2
                tail = tail.next
                current2 = current2.next

        if current1:
            tail.next = current1
        if current2:
            tail.next = current2
        
        return dummy.next
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

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

    res = llist1.merge_list(llist2.head)
    
    llist3 = LinkedList()
    llist3.head = res
    llist3.display()