"""
Given a singly linked list, determine if it is a palindrome
"""

class Solution(object):
	def isPalindrome(self, head):
		fast = slow = head 
		# Move slow to the middle of the list
		while fast and slow: 
			fast = fast.next.next
			slow = slow.next 
		# Reverse second half 
		node = None
		while slow:
			nxt = slow.next
			# Make slow.next None/end
			slow.next = node
			node = slow 
			slow = nxt

		while node:
			if node.val != head.val:
				return False
			node = node.next
			head = head.next
		return True


