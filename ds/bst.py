class Node(object):
	def __init__(self, val):
		self.data = val
		self.left = None
		self.right = None

class BST(object):
	def __init__(self):
		self.head = None

	def insert(self,root,node):
		if root is None:
			root = node
		else:
			if root.data < node.data:
				if root.right is None:
					root.right = node
				else:
					insert(root.right, node)
			else:
				if root.left is None:
					root.left = node
				else:
					insert(root.left, node)

	def search(self,root, key):
		if root is None or root.val == key:
			return root

		# if root.data is less than the key, we must search on the right
		if root.data < key:
			return search(root.right, key)
		return search(root.left, key)

	def inorder(self,root):
		if root:
			self.inorder(root.left)
			print(root.data)
			self.inorder(root.right)

if __name__ == '__main__':
	root = Node(5)
	root.insert(root, Node(3))
	root.insert(root, Node(2))
	root.insert(root, Node(7))
	root.insert(root, Node(6))
	root.insert(root, Node(8))
	root.inorder(root)