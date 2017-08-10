"""
Palindrome: Implement a function to check if a linked list is a palindrome

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

def run(llist):
	if(palindrome(llist)):
		print("Yes, it's a palindrome.")
	else:
		print("Nope! Not a palindrome")

def print_list(sing_list):
	tmp = sing_list
	while(tmp):
		print(tmp.data, end="->")
		tmp = tmp.next
	print("END")

def palindrome(llist):
	print_list(llist)
	print("Checking if palindrome")
	prev = None
	current = llist
	# Reverse the list
	# Three way swap.
	while(current):
		next = current.next
		current.next = prev
		prev = current
		current = next
	reversed_list = prev
	print_list(reversed_list)

	# Traverse both lists at the same time. Check if reversed is same as original.
	while(llist):
		print(str(llist.data) + " vs " + str(reversed_list.data))
		if llist.data != reversed_list.data:
			return False
		llist = llist.next
		reversed_list = reversed_list.next
	return True

llist = Node(3)
vals = [5,8,7,8,5,3]
for x in vals:
	llist.append(x)
run(llist)