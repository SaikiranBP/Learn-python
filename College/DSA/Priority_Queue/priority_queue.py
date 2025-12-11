class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class Priority_queue:
    
    def __init__(self):
        self.front = None
        
    def enqueue(self, value, order):
        new_node = Node(value, order)
        # if queue is empty new node has higher priority than front
        if (self.front is None) or (order > self.front.priority):
            new_node.next = self.front
            self.front = new_node
        else:
            # if queue is not empty new node’s priority is not higher than front.
            temp = self.front
            while (temp.next) and (temp.next.priority >= order):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            return

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return
        removed_element = self.front.data
        self.front = self.front.next
        return removed_element
    
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return
        return self.front.data
    
p1 = Priority_queue()

while True:
    
    print("---Priority Queue using Linked list---")
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
        print("Enter the priority order")
        inp_priority = int(input())
        p1.enqueue(value, inp_priority)
        print("Inserted", value)
        
    if choice == 2:
        p1.dequeue()
        
    if choice == 3:
        p1.peek()
        
    if choice == 4:
        p1.display()
        
    if choice == 5:
        print("Exiting....")
        break
    
    else:
        print("Choose the correct option")