#Node class. Simple pointers
class Node: 
	def __init__(self, data):
		self.data = data 
		self.next = None #initialize with null next pointer

	def __str__(self):
		print(self.data)

#LinkedList class
class LinkedList: 
	def __init__(self):
		self.head = None

	# in order traversal of the list, print each node
	def print_list(self):
		node = self.head
		while(node):
			print(node.data)
			node = node.next

	# add a node to the front of the list
	# must add node, set head as next, set node as head
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# add another node immediately following the supplied node
	def insert_after(self, prev_node, new_data):
		if prev_node is None: 
			print("Given previous node is null.")
			return

		# Create a new node, place like so: prev -> new -> prev.next
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	# Add a new node at the end of the list 
	def append(self, new_data):
		new_node = Node(new_data)
		new_node.next = None

		# create a node for traversal
		temp = self.head
		while temp.next is not None:
			temp = temp.next

		temp.next = new_node



if __name__=='__main__':
	llist = LinkedList()
	llist.head = Node(5)
	second = Node(3)
	third = Node(2)

	llist.head.next = second
	second.next = third
	llist.push(6)
	llist.append(12)
	llist.insert_after(second, 7)
	llist.print_list()