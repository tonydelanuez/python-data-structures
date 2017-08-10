class Node(object):
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

def preorder(node):
	if(node):
		print(node.data)
		preorder(node.left)
		preorder(node.right)