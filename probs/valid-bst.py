import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# With this solution, we take the largest and smallest possible integer values. 
# From there, we check if the parent is null. If the parent is null (from call from our helper function), we've reached the end of the tree without returning an error. Return true. Otherwise, we must make two recursive calls and two checks to make sure we're still adhering to p)
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(p, low, high):
            if(p == None):
                return True
            return (p.val > low) and (p.val < high) and valid(p.left, low, p.val) and valid(p.right, p.val, high)
        
        return valid(root, -sys.maxint - 1, sys.maxint)