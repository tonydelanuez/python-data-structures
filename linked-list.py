#Node class

class Node: 
	def __init__(self, data):
		self.data = data 
		self.next = None #initialize with null next pointer

	def __str__(self):
		print(self.data)

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


if __name__=='__main__':
	llist = LinkedList()
	llist.head = Node(5)
	second = Node(3)
	third = Node(2)

	llist.head.next = second
	second.next = third
	llist.push(6)
	llist.print_list()