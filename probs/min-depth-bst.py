class Solution(object):
	def minDepth(self, root):
		if root == None: 
			return 0
		if root.left == None: 
			return minDepth(root.right) + 1
		if root.right == None: 
			return minDepth(root.left) + 1
		return min(minDepth(root.left), minDepth(root.right)) + 1