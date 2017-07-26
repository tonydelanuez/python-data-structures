import sys

class Stack(object):
	# Push an object onto the stack, check min
	def push(self, x):
		if(len(self.array)) == 0:
			self.min = x
		if x < self.min:
			self.min = x
		self.array.append(x)

	# Pop an element from the stack 
	def pop(self):
		tmp = self.array[-1]
		del self.array[-1]
		return tmp

	# Peek at the top element of the stack 
	def top(self):
		return self.array[-1]

	# Get the minimum element from the stack
	def getMin(self):
		return self.min

	def __init__(self):
		self.array = []
		self.min = 0

temp = Stack()
temp.push(10)
temp.push(13)
temp.push(9)
temp.push(15)
print(temp.getMin())
print(temp.pop())
print(temp.top())