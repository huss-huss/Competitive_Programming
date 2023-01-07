class MyQueue(object):

    def __init__(self):
        self.stack = []    

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        popped = self.stack[0]
        self.stack.remove(self.stack[0])
        return popped
        

    def peek(self):
        return self.stack[0]

    def empty(self) :
        return self.stack == []
        
  
    
  
