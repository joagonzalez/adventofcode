class Stack():
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return f'Stack elements: {self.stack} - Stack size: {self.size()}'    
    
    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return None
    
    def push(self, value):
        self.stack.append(value)
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        if self.size() == 0:
            return True
        else:
            return False
    