

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0    
    
    def push(self, value):
        self.items.append(value)

    def pop(self): 
        if self.is_empty():
            return None
        poppedItem = self.get_stack_peek()
        self.items.pop()
        return poppedItem
    
    def get_stack_peek(self):
        return self.items[-1]
    
    def get_stack_size(self):
        return len(self.items) 
    
    def get_all_stack_items(self):
        return self.items
    
    