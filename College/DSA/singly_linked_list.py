""" 
Singly Linked List
Operations : Insert at Beginning, Insert at End, delete by value
Insert after some speicfic value, print the list
"""

class Node:
    # Creating a new Node
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        # inserting the new node at beginning
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        # inserting the new node at end of the linked list
        new_node = Node(data)
        
        # case 1: List is empty
        if self.head is None:
            self.head = new_node
            return

        # case 2: List is not empty
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def insert_after_value(self, target, value):
        # inserting the new node after some specific node
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            
    def delete_by_value(self, value):
        # deleteing the head node
        if self.head == value:
            self.head = self.head.next
            return
        
        # deleting the node if it is at some other position
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        
        if current.next is None:
            return False
        # Linking the previous node to the next node
        current.next = current.next.next
        return
            
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end= " -> ")
            current = current.next
        print("None")


# creating an object
l1 = Linkedlist()
l1.insert_at_beginning(10)
l1.insert_at_end(20)
l1.insert_at_beginning(5)
l1.insert_at_end(30)
l1.insert_after_value(20, 25)
l1.print_list()
l1.delete_by_value(30)
l1.print_list()