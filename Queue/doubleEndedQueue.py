### Double Ended Queue is a data structure that allows insertion and deletion of elements from both ends (front and rear) of the queue. It is also known as Deque (Double Ended Queue). 
### In a double ended queue, we can perform the following operations:
### 1. insertFront(value): Inserts an element at the front of the queue.  
### 2. insertRear(value): Inserts an element at the rear of the queue.
### 3. deleteFront(): Deletes an element from the front of the queue.
### 4. deleteRear(): Deletes an element from the rear of the queue.
  
class Dequeue:
  def __init__(self):
    self.queue = []
    
  def isEmpty(self):
    return len(self.queue) == 0
  
  def lenQueue(self):
    return len(self.queue)
  
  
  def insertAtEnd(self,value):
    self.queue.append(value)
    
  def deleteAtFront(self):
    if not self.isEmpty():
      return self.queue.pop(0)
    else:
      return "Queue is empty"
    
  def insertAtFront(self,value):
    self.queue.insert(0,value)
  
  def deleteAtEnd(self):
    if not self.isEmpty():
      return self.queue.pop()
    else:
      return "Queue is empty"
    
dq = Dequeue()
dq.insertAtEnd(10)
dq.insertAtEnd(20)
dq.insertAtFront(5)
print(dq.deleteAtFront())
print(dq.deleteAtEnd())
print(dq.deleteAtFront())
