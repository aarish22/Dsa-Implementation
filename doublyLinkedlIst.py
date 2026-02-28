class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None
    self.prev = None
    
class DoublyLinkedList:
  def __init__ (self):
    self.head = None
    
  def insertAtEnd(self,data):
    temp = Node(data)
    if self.head == None:
      self.head = temp
      return
    else:
      t1 = self.head
      while t1.next != None:
        t1 = t1.next
      t1.next = temp 
      