### circular queue implementation using list
## font == rear == -1
## first element is added rear = 0 and front = 0

class CircularQueue:
  def __init__(self,size):
    self.queue = [0] * size
    self.size = size
    self.front = -1
    self.rear = -1
  
  def isEmpty(self):
    return self.front == -1 and self.rear == -1 ## both front and rear are -1 then queue is empty
  
  def isFull(self):
    return (self.rear + 1) % self.size == self.front ## if rear is just before front then queue is full
  
  def enqueue(self,value):
    if self.isFull():
      return "Queue is full"
    elif self.isEmpty():
      self.front = 0
      self.rear = 0
      self.queue[self.rear] = value
    else:
      self.rear = (self.rear + 1) % self.size
      self.queue[self.rear] = value
      
  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    elif self.front == self.rear: ## only one element in the queue
      value = self.queue[self.front]
      self.front = -1
      self.rear = -1
      return value
    else:
      value = self.queue[self.front]
      self.front = (self.front + 1) % self.size
      return value
    
  def frontElement(self):
    if self.isEmpty():
      return "Queue is empty"
    else:
      return self.queue[self.front]
  
  def rearElement(self):
    if self.isEmpty():
      return "Queue is empty"
    else:
      return self.queue[self.rear]
    
  def lenQueue(self):
    if self.isEmpty():
      return 0
    elif self.rear >= self.front:
      return self.rear - self.front + 1
    else:
      return self.size - (self.front - self.rear - 1)
cq = CircularQueue(5)
cq.enqueue(10)    
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
print(cq.enqueue(60)) ## queue is full
print(cq.dequeue())
print(cq.dequeue())
cq.enqueue(60)
print(cq.dequeue())
print(cq.frontElement())
print(cq.rearElement())
print(cq.lenQueue())