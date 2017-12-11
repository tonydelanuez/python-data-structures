class Node(object):
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None
# Inorder traversal. Visit the left branch, head, right branch.

def inorder(node):
	if(node):
		inorder(node.left)
		print(node.data)
		inorder(node.right)
	

