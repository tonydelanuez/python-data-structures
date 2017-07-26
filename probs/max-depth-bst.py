class Solution(object):
	def maxDepthBST(self, node):
		if node == None:
			return 0
		else:
			return max(maxDepthBST(node.left), maxDepthBST(node.right)) + 1

