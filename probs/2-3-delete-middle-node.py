"""
Delete Middle Node: 
Implement an algorithm to delete a node in the middle (i.e. any node but the first or the last, not necessarily the exact middle) of a singly linked list, given only access to that node. 
"""


class Node(object):
	def __init__(self, val):
		self.data = val
		self.next = None

def delete_one(llist, val):
	slow = None
	fast = llist
	# Stop when fast is the node we want to delete. 
	while fast.data != val:
		slow = fast
		fast = fast.next

	# Skip over the node
	slow.next = fast.next
	fast.next = fast.next.next
	


# I did it this way because it looks cool and it's 11:20 at night. I know I could have iterated. 
def simulate(mode=""):
	head = Node(5)
	head.next = Node(3)
	head.next.next = Node(2)
	head.next.next.next = Node(7)
	head.next.next.next.next = Node(6)
	head.next.next.next.next.next = Node(8)
	if mode=="delete":
		delete_one(head, 2)
	temp = head
	while(temp):
		print(temp.data, end="->")
		temp = temp.next
	print("END")

print("Unedited List:")
simulate()

del_val = 2
print("List after deleting value: " + str(del_val))
simulate("delete")

