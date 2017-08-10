"""
Write code to partition a linked list around a value x such that all nodes less than x come before all nodes greater than or equal to x. 
If x is contained within the list, the values of x only need to be after the elements less than x. The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions. 


EXAMPLE:
Input: 3 -> 5 -> 8 -> 5-> 10 -> 2-> -> 1 [partition = 5]

My implementation: 
maintain an end pointer, make swaps, decrement end pointer.




Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

"""

class Node(object):
	def __init__(self,val):
		self.data = val
		self.next = None

	def append(self,d):
		end = Node(d)
		n = self
		while (n.next != None):
			n = n.next
		n.next = end

def partition(node, value):
	print("Partitioning around: " + str(value))
	# Keep two separate lists to track the larger and smaller elements. 
	head = node
	tail = node 
	while(node):
		next = node.next
		if node.data < value:
		# Insert node at head, in-place swap.
			node.next = head
			head = node
		else:
			# Add the element to the end of the list
			tail.next = node
			# update tail to reflect it is at end
			tail = node
		node = next
	# Set the tail to None like a proper Linked List
	tail.next = None
	# Return the list we created 
	return head

def run():
	#3 -> 5 -> 8 -> 5-> 10 -> 2-> -> 1
	llist = Node(3)
	vals = [5,8,5,10,2,1]
	for x in vals:
		llist.append(x)
	t = partition(llist, 5)
	while(t):
		print(t.data, end="->")
		t = t.next
	print("END")

run()