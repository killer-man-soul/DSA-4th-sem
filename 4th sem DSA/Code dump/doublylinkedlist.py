class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node

    def delete_node_by_key(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                if current_node is self.head:
                    self.head = current_node.next
                    if self.head:
                        self.head.prev = None
                elif current_node is self.tail:
                    self.tail = current_node.prev
                    self.tail.next = None
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                return True
            current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

dll=DoublyLinkedList()
dll.add_node(11)
dll.add_node(3)
dll.add_node(6)
dll.add_node(26)
dll.add_node(15)
dll.add_node(7)
dll.print_list()
dll.delete_node_by_key(7)
dll.print_list()
