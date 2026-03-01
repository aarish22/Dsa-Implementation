### front = rear = -1
### first element is added rear = 0 and front = 0
### second element is added rear = 1 and front = 0
### insert => rear = (rear + 1) % size(to avoid overflow)
### delete => front = (front + 1) % size(to avoid underflow)
### append <-- insert at rear
## pop(0) <-- delete at front


class Queue:
  def __init__(self):
    self.queue = []
    
  def isEmpty(self):
    return len(self.queue) == 0
  
  def lenQueue(self):
    return len(self.queue)
  
  
  def enqueue(self,value):
    self.queue.append(value)
    
  def dequeue(self):
    if not self.isEmpty():
      return self.queue.pop(0)
    else:
      return "Queue is empty"
    

q = Queue()
q.enqueue(10)   
q.enqueue(20)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.dequeue()
  
  