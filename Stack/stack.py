## Stack is a linear data structure which follows the principle of Last In First Out (LIFO). The last element added to the stack will be the first one to be removed. The main operations of a stack are push (to add an element), pop (to remove an element), and peek (to view the top element without removing it).


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