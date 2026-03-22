## bst search is similar to bst insertion but instead of inserting we are searching for the value in the tree and returning true if found and false if not found.
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BST:
  def __init__(self):
    self.root = None
  
  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
    else:
      self._insert_recursive(self.root, value)
  
  def _insert_recursive(self, current_node, value):
    if value < current_node.value:
      if current_node.left is None:
        current_node.left = Node(value)
      else:
        self._insert_recursive(current_node.left, value)
    else:
      if current_node.right is None:
        current_node.right = Node(value)
      else:
        self._insert_recursive(current_node.right, value)


def inorder_traversal(node):
  if node is not None:
    inorder_traversal(node.left)
    print(node.value, end=' ')
    inorder_traversal(node.right)

def search_bst(node, target):
  if node is None:
    return False
  if node.value == target:
    return True
  elif target<node.value:
    return search_bst(node.left, target)
  else:
    return search_bst(node.right, target)

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

print("Inorder Traversal of BST:")
inorder_traversal(bst.root)

 

  