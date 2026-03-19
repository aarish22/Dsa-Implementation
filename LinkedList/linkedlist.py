## Linked List is a linear data structure where each element is a separate object. Each element (node) of a list is comprising of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference.

class Node:
  def __init__ (self,data,next=None):
    self.data = data
    self.next = next
  
class SinglyLinkedList:
  def __init__(self,head=None):
    self.head = head
    
  def inserAtEnd(self,value):
    temp = Node(value)  ## creating a new node with the value to be inserted and next as None
    if self.head != None:
      t1 = self.head
      while t1.next != None:
        t1 = t1.next
      t1.next = temp
    else:
      self.head = temp
      
  def insertAtBegin(self,value):
    temp = Node(value)  ## creating a new node with the value to be inserted and next as None
    if self.head != None:
      temp.next = self.head
      self.head = temp
    else:
      self.head = temp
      
  def insertAtPos(self,value,x):
    temp = Node(value)
    t1 = self.head
    while t1.next!= None:
      if t1.data == x:
        temp.next = t1.next  
        t1.next = temp
      t1 = t1.next
      
  def deleteLL(self, x):
    curr = self.head
    prev = None
    while curr != None:
      if curr.data == x:
        if prev == None:
          self.head = curr.next
        else:
          prev.next = curr.next
        return
      else:
        prev = curr
        curr = curr.next
        
  def printLL(self):
    temp = self.head
    while temp != None:
      print(temp.data,end=" ")
      temp = temp.next

obj = SinglyLinkedList()
obj.inserAtEnd(10)
obj.inserAtEnd(20) 
obj.inserAtEnd(30)
obj.inserAtEnd(40)
obj.inserAtEnd(50)
obj.insertAtBegin(5)
obj.insertAtPos(25,20)

obj.deleteLL(50)
obj.printLL()