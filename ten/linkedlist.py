class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            
    def get(self, index):
        current = self.head
        
        for _ in range(index):
            if current.next is not None:
                current = current.next
                
        return current.value
    
    def insert_at(self, idx, value):
        current = self.head
        
        for _ in range(idx-1):
            if current.next is not None:
                current = current.next
                
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node
        
    def remove_at(self, idx):
        current = self.head
        for _ in range(idx - 1):
            current = current.next
            
        # remove_node = Node(current.next)
        remove_node = current.next
        current.next = remove_node.next
        remove_node.next = None
            
first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third 

first.value = 6

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.get(0)
ll.get(1)
ll.get(3)
