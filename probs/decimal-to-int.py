"""
	Given an integer x, return the binary representation of x

"""

class Solution(object):
	def decimalToInt(self, x):
		bit_stack = []
		while x > 0:
			# Determine if LSB 1 or 0, add to bit stack
			bit_stack.append(str(x % 2))
			# Right shift the number
			x = x >> 1
		print("".join(bit_stack[::-1]))


num = 14
test = Solution();
test.decimalToInt(num)