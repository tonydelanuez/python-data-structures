class DynamicArray:
		# Set interal size equal to 0 and make an array of initial_length.
	def __init__(self, initial_length):
		self.length = 0
		self.array = [None] * initial_length

	def add(self, data):
		# If we've reached max capacity in the underlying array, grow
		if self.length == len(self.array):
			self.grow()
		else:
		# Otherwise just place data at length and post increment
			self.array[self.length] = data
			self.length += 1

	# Double the size of the array 
	def grow(self):
		new_array = [None] * 2 * self.length
		for index,val in enumerate(self.array):
			new_array[index] = self.array[index]
		self.array = new_array

	# Use end to not print on different line 
	def print_elements(self):
		print("[", end="")
		for index in range(self.length):
			print( str(self.array[index]) + " ",end="")
		print("]")

darray = DynamicArray(4)
darray.add(5)
darray.add(7)
darray.add(6)
darray.add(5)
darray.add(7)
darray.add(6)
darray.add(8)
darray.add(5)
darray.add(7)
darray.add(6)
darray.add(8)
darray.add(8)
darray.add(5)
darray.add(7)
darray.add(6)
darray.add(8)
darray.print_elements()

