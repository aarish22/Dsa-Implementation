class Node:
  def __init__(self, value):
    self.value = value
    self.left = None  
    self.right = None


## pre-order
def preOrder(root):
  if root is not None:
    print(root.value, end =", ")
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
  if root is not None:
    inOrder(root.left)
    print(root.value, end=",")
    inOrder(root.right)

def postOrder(root):
  if root is not None:
    inOrder(root.right)
    postOrder(root.left)
    print(root.value, end=",")


    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

preOrder(root)
