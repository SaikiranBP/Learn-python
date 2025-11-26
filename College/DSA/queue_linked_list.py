import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, value):
        # Inserts the element into the queue
        new_node = Node(value)
        if self.rear is None:
            # if queue is empty
            self.rear = new_node
            self.front = new_node
        else:
            # is queue is not empty
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        # Pops out the last element from the queue
        if self.front is None:
            # if queue is empty
            print("Queue is empty")
            return
        
        # if queue is not empty
        temp = self.front
        self.front = temp.next
        if self.rear is None:
            self.rear = None
        return ("Popped value:", temp.data)
    
    def peek(self):
        # Peeks the first element of the queue
        if self.front is None:
            print("Queue is empty")
            return
        print(self.front.data)
    
    def display(self):
        # Displays the elements of the queue
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
            time.sleep(1.5)
        print("None")

# Creating an object
queue = Queue()

while True:
    
    print("---Queue using Linked list---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    print("Enter your choice")
    
    try:
        choice = int(input())
    except ValueError:
        print("Invalid Choice")
        continue
    
    if choice == 1:
        print("Enter the value")
        value = int(input())
        queue.enqueue(value)
        print("Inserted", value)
        
    if choice == 2:
        queue.dequeue()
        
    if choice == 3:
        queue.peek()
        
    if choice == 4:
        queue.display()
        
    if choice == 5:
        print("Exiting....")
        time.sleep(1.5)
        break