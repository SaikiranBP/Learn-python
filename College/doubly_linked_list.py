"""Doubly Linked List"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    
    def insert_after_value(self, target, value):
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(value) # create a new node
                # adjust the references
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
        print("Value not found")
    
    def delete_by_value(self, value):
        # if list is empty
        if self.head is None:
            return "List is empty"
        
        currrent = self.head
        while currrent:
            if currrent.data == value:
                # if deleteing head
                if currrent.prev:
                    currrent.prev.next = currrent.next
                else:
                    self.head = currrent.next
                # updating next node's prev
                if currrent.next:
                    currrent.next.prev = currrent.prev
                return
            currrent = currrent.next
        
        print("Value not found")
        
    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        
    def print_backward(self):
        current = self.head
        if current is None:
            return "List is empty"
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
        
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(5)
dll.insert_after_value(20, 25)

dll.print_forward()   
dll.print_backward()   
dll.delete_by_value(25)
dll.print_forward()    
        