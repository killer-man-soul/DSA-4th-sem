
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

   
    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)

        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

       
        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        self.head = new_node
        current.next = self.head

    
    def insert_at_end(self, new_data):
        new_node = Node(new_data)

        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        
        current = self.head
        while current.next != self.head:
            current = current.next

        
        current.next = new_node
        new_node.next = self.head

   
    def delete(self, key):
        
        if self.head is None:
            return

        
        current = self.head
        prev = None
        while current.data != key:
            if current.next == self.head:
                print("Key not found in the list")
                return
            prev = current
            current = current.next

        
        if current == self.head:
            
            if current.next == self.head:
                self.head = None
           
            else:
                current.next = self.head.next
                self.head = self.head.next
      
        else:
            prev.next = current.next

    
    def print_list(self):
        
        if self.head is None:
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()


cll = CircularLinkedList()


cll.insert_at_beginning(3)
cll.insert_at_beginning(2)
cll.insert_at_beginning(1)
cll.insert_at_end(4)
cll.insert_at_end(5)
cll.print_list()
print()
cll.delete(4)
cll.print_list() 