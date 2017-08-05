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
			print(str(node.data), end="->")
			node = node.next
		print ("END")

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
		while temp.next:
			temp = temp.next

		temp.next = new_node

	# Get the size of the current list 
	def size(self):
		temp = self.head
		count = 0
		while temp: 
			count += 1
			temp = temp.next
		return count

	# Linear time search on singly linked list
	def search(self, data):
		temp = self.head
		found = False
		while temp and found is False:
			if temp.val == data:
				found = True
			else:
				temp = temp.next
		print("Couldn't find the value: " + str(data))
		return found

	# Similar to search -- look for the element then delete it. (Deletes first occurrence)
	def delete(self, data):
		print("Deleting " + str(data) + " from list: ")
		self.print_list()
		print("")
		temp = self.head
		found = False
		previous = None
		while temp and found is False: 
			if temp.data == data:
				found = True
			else:
				previous = temp
				temp = temp.next
		if temp is None:
			print("Value " + str(data) + "is not in list")
		if previous is None:
			self.head = temp.next
		else:
			previous.next = temp.next

	# Reverse the linked list. Perform a three way shuffle/swap
	def reverse(self):
		print("Reversing list...")
		current = self.head
		previous = None
		while current: 
			next = current.next
			current.next = previous
			previous = current
			current = next
		self.head = previous

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
	llist.append(15)
	llist.append(18)
	for i in range(10):
		llist.append(i)
	llist.delete(8)
	llist.print_list()
	print("")
	print("Size: " + str(llist.size()))
	llist.reverse()
	llist.print_list()
	print("Size: " + str(llist.size()))