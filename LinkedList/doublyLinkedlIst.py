class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None
    self.prev = None
    
class DoublyLinkedList:
  def __init__ (self):
    self.head = None
    
    
  def isnertAtBegin(self,data):
    temp = Node(data)
    if self.head == None:
      self.head = temp
      return
    else:
      temp.next = self.head
      self.head.prev = temp
      self.head = temp
    
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
      temp.prev = t1
  
  def insertAtPos(self,data,x):
    if self.head == None:
      return f"List is empty"
    t1 = self.head
    while t1 and t1.data != x:
      t1 = t1.next
    if t1 is None:
      return f"{x} is not present in the list"
    
    temp = Node(data)
    temp.next = t1.next
    temp.prev = t1  
    if t1.next:
      t1.next.prev = temp
    t1.next = temp
  
  def deleteDLL(self,x):
    if self.head == None:
      return f"List is empty"
    t1 = self.head
    while t1 and t1.data != x:
        t1 = t1.next
    if t1 is None:
      return f"{x} is not present in the list"
    if t1.prev == None:
      self.head = t1.next
      if self.head:
        self.head.prev = None
      return
    else:
      t1.prev.next = t1.next
    if t1.next:
      t1.next.prev = t1.prev

  
  def printDLL(self):
    temp = self.head
    while temp != None:
      print(temp.data,end=" <--> ")
      temp = temp.next
      
        
obj = DoublyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20) 
obj.insertAtEnd(30)
obj.insertAtEnd(4)
obj.isnertAtBegin(5)
obj.insertAtPos(15,20)
obj.deleteDLL(4)
obj.printDLL()