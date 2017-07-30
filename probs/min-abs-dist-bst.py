"""
Minimum Absolute Difference in BST

Given a binary search tree with non-negative values,
find the minimum absolute difference between values of any two nodes. 

Example:
	1 
	  \ 
	    3
	   /
	  2

The minimum absolute difference is 1, which is the difference between 2 and 1

"""
class Solution(object):
	# Since this is a BST, inorder traversal results in sorted values.
	def minimumAbsDiffBST(self,root):
		# Create an array of the sorted values with an inorder traversal
		def inorder(node, vals=[]):
			if node.left:
				inorder(node.left, vals)
			vals.append(node.val)
			if node.right:
				inorder(node.right, vals)
			return vals
		# Run an inorder traversal on the root.
		vals = inorder(root)
		return min([abs(a-b) for a,b in zip(vals, vals[1:])])

