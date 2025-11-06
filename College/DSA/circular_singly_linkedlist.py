"""
This program is about Circular Singly Linked list program 
and it performs following opeartions: Insert at Beginning, 
insert at End, delete by value, displaying the list
"""

class Node:
    # Creating a new node
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_Singly_LL:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, value):
        # Inserts the new node at the beginning of the list
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, value):
        # Inserts the new node at the end of the list
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return

        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head        
        
    def delete_by_value(self, value):
        # Delete the node
        # Case1: If the list is empty
        if self.head is None:
            return "List is empty"
        current = self.head
        while True:
            if current.data == value:
                # Case2: If the delete node is at 1st position
                if current.next == self.head:
                    self.head = None
                    return
                last = self.head
                while last.next != self.head:
                    last = last.next
                last.next = self.head.next
                self.head = self.head.next
                return
            prev = current
            current = current.next
            if current.data == value:
                prev.next = current.next 
                return
            if current == self.head:
                break
        print("Value not found")
    
    def print_list(self):
        # Displays the elements of the list
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" --> ")
            current = current.next
            if current == self.head:
                break
        print(" Back to Head ")  

# Creating an object of the class
cll = Circular_Singly_LL()
cll.insert_at_beginning(5)
cll.insert_at_beginning(10)

cll.insert_at_end(20)
cll.insert_at_end(30)

cll.print_list()

cll.delete_by_value(20)
cll.print_list()