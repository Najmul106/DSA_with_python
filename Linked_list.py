class node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        # empty linked list
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

    def insert_head(self, value):
        new_node = node(value)
        # create connection
        new_node.next = self.head
        # reassign head
        self.head = new_node
        # increment n
        self.n = self.n + 1

    def append(self, value):
        new_node = node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return 
        curr = self.head
        while curr.next != None:
            curr = curr.next
        # you are at the last node
        curr.next = new_node
        self.n = self.n + 1

    def insert_after(self, after, value):
        new_node = node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return "item not found "

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            # empty
            return "Empty LL"
        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):
        if self.head == None: # Fixed typo here from 'heda'
            return "Empty LL"
        curr = self.head
        if curr.next == None:
            return self.delete_head()
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n = self.n - 1

    def remove(self, value):
        if self.head == None:
            return "Empty LL"
        if self.head.data == value:
            self.delete_head() # Fixed missing parentheses
            return
        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr.next == None:
            return "Not Found"
        else:
            curr.next = curr.next.next
            self.n = self.n - 1 # Ensure length is updated

    def search(self, item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return "Not Found"

    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1
        return "IndexError"

    # THIS IS NOW PROPERLY INDENTED INSIDE THE CLASS
    def RemoveByIndex(self, index):
        if self.head == None:
            return "Empty LL"
            
        if index == 0:
            self.delete_head()
            return "Removed head"
            
        curr = self.head
        pos = 0
        
        # Stop one node BEFORE the one we want to remove
        while curr != None and curr.next != None:
            if pos == index - 1:
                curr.next = curr.next.next
                self.n = self.n - 1
                return "Removed item"
            curr = curr.next
            pos = pos + 1
            
        return "IndexError"
        
           
# --- Testing the code ---
l = LinkedList()
l.append(1)
l.append(3)
l.append(5)

print("List before:", l)

new_var = l.RemoveByIndex(0)

print("Return message:", new_var)
print("List after:", l)