class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Circular_Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        
    def enqueue(self, value):
        new_node = Node(value)
        # If queue is empty
        if self.front is None:
            self.rear = self.front = new_node
            self.rear.next = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            new_node.next = self.front
    
    def dequeue(self):
        # If queue is empty
        if self.front is None:
            print("Queue is empty")
            return
        # If queue has only one node
        if self.front == self.rear:
            temp = self.front
            self.front = self.rear = None
            return temp.data
        
        # If queue has more than one node
        temp = self.front
        self.front = temp.next
        self.rear.next = self.front
        return temp.data
    
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while True:
            print(temp.data, end=" -> ")
            if temp == self.rear:
                break
            temp = temp.next
        print("(Back to front)")

q = Circular_Queue()

while True:
    
    print("---Circular Queue using Linked list---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    print("Enter your choice")
    
    try:
        choice = int(input())
    except ValueError:
        print("Invalid Choice")
        continue
    
    if choice == 1:
        print("Enter the value")
        inp_value = int(input())
        q.enqueue(inp_value)
        print("Inserted", inp_value)
        
    if choice == 2:
        q.dequeue()

    if choice == 3:
        q.display()
        
    if choice == 4:
        print("Exiting....")
        break
    
    else:
        print("Choose the correct option")