class Stack(object):
	# Create the underlying array
	def __init__(self):
		self.arr = []

	# Pop the last element from the stack. Delete and return it.
	def pop(self):
		if len(self.arr) < 1:
			return False
		tmp = self.arr[-1]
		del self.arr[-1]
		return tmp
 
 	# Push a value onto the stack
	def push(self, val):
		self.arr.append(val)

	def is_empty(self):
		return len(self.arr) == 0

	def peek(self):
		return self.arr[-1]

def run():
	test = Stack()
	for i in range(15):
		print("Pushing number: " + str(i))
		test.push(i)
	print("Peeking at top of stack")
	print(test.peek())
	print("Is stack empty? " + str(test.is_empty()))
	print("Popping values...")
	while(not test.is_empty()):
		print(test.pop())
	print("Emptied the stack!")
	# Extra pop to test failure case.
	test.pop()
run()