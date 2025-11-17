#compare dung de quy
class Node:
    def __init__(self, data):
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
    
def compare_list(head1, head2):

    if head1 is None and head2 is None:
        return 1
    
    if head1 is None or head2 is None:
        return 0
    
    if head1.data != head2.data:
        return 0
    
    return compare_list(head1.next, head2.next)


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

    res = compare_list(llist1.head, llist2.head)
    print(res)