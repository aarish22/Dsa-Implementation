## bst traversal is a way to visit all the nodes in a binary search tree in a specific order. There are three types of bst traversal: pre-order, in-order and post-order. In pre-order traversal, we visit the root node first, then the left subtree and finally the right subtree. In in-order traversal, we visit the left subtree first, then the root node and finally the right subtree. In post-order traversal, we visit the left subtree first, then the right subtree and finally the root node.

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
    print(root.value, end=", ")
    inOrder(root.right)

def postOrder(root):
  if root is not None:
    postOrder(root.right)
    postOrder(root.left)
    print(root.value, end=", ")


    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

preOrder(root)
print()
inOrder(root)
print()
postOrder(root)
