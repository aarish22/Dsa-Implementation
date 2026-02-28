class Stack:
  def __init__(self):
    self.stack = []
  
  def lenStack(self):
    return len(self.stack)    

  def push(self,value):
    self.stack.append(value)
    
  def peek(self):
    if self.lenStack()>0:
      return self.stack[-1]
    else:
      return "Stack is empty"
    
  def pop(self):
    if self.lenStack()>0:
      return self.stack.pop()
    else:
      return "Stack is empty"
    
stk = Stack()
stk.push(10)
stk.push(20)
print(stk.peek())
print(stk.pop())