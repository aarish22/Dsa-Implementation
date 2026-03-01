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
    

  