from xxlimited import new


class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        if self.head is None:
            print("list is empty")
        return 
    
    def traverse(self):
        n = self.head
        while n is not None:
            print(n.data)
            n = n.ref

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None: # list is empty 
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
        return 
    
    def insert_after_node(self, data, choose_node):
        n = self.head
        while n is not None:
            if choose_node == n.data:
                break
            else:
                n = n.ref
        if n is None:
            print("element not in list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref 
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("list is empty")
            return 
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("list is empty")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        
    def insert_in_empty_ll(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        else:
            print("list is not empty")
            
    def delete_node(self):
        if self.head is None:
            print("cannot delete the node, list is empty")
        elif self.head.ref is None:
            self.head = None # list is empty
        else:
            self.head = self.head.ref

    def delete_last_node(self):
        if self.head is None:
            print("list is empty, nothing to delete")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref # this is the second last node. 
            n.ref = None

    def delete_by_value(self, x):
        n = self.head
        if n is None:
            print("list is empty and nothing to delete")
            return
        if n.data == x: #check if the given node is 1st node:
            print("this is the 1st node")
            n = n.ref
            return
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("node not found!")
        else:
            n.ref = n.ref.ref
            return

    def length(self):
        total = 0
        n = self.head
        if n is None:
            return total
        while n is not None:
            n = n.ref
            total += 1
        return total

ll = LinkedList()

# ll.insert_in_empty_ll(1)
for i in range(0,5):
    ll.insert_at_head(i)
ll.add_before(2,8)
print("list length is ", ll.length())
ll.traverse()

        
            