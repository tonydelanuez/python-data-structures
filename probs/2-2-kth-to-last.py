"""
Return Kth to Last:
Implement an algorithm to find the kth to last element of a singly linked list
"""

class Node(object):
	def __init__(self, x):
		self.val = x
		self.next = None
 
# Solution to this problem is to have a pointer with a head start. 
# Advance it k times before progressing both the main pointer and this pointer.
# The early pointer will reach the end of the list and the lazy pointer will be at n-k
def kth_to_last(node, k):
	tmp = node
	for i in range(k):
		tmp = tmp.next
	while tmp:
		tmp = tmp.next
		node = node.next
	return node.val


test = Node(1)
dummy = Node(0)
dummy.next = test

for i in range(2,100):
	test.next = Node(i)
	test = test.next

print(kth_to_last(dummy, 3))

