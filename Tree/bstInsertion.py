## bst insertion is the process of adding a new node to a binary search tree while maintaining the properties of the tree. The properties of a binary search tree are that the left subtree of a node contains only nodes with values less than the node's value, and the right subtree of a node contains only nodes with values greater than the node's value. To insert a new node into a binary search tree, we start at the root and compare the value of the new node with the value of the current node. If the value of the new node is less than the value of the current node, we move to the left child of the current node. If the value of the new node is greater than or equal to the value of the current node, we move to the right child of the current node. We repeat this process until we find an empty spot where we can insert the new node.
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

 

  