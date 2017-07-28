# Evaluate the value of an arithmetic expression in Reverse Polish Notation. 
# Valid operators are +, -, *, /.
# Each operand may be an integer or another expression. 
# Some examples:
# ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ["4", "13", "5", "/", "+"] -> (4 + (13/5)) -> 6

class Solution(object):
	def reversePolish(self, arr):
		stack = []
		for index, val in enumerate(arr):
			print("Current stack: " + str(stack))
			if val == "+":
				#
				x = int(stack.pop(-1))
				y = int(stack.pop(-1))
				print("Evaluating: " + str(x) + " " + val + " " + str(y))
				stack.append(x+y)
			elif val == "-":
				#
				x = int(stack.pop(-1))
				y = int(stack.pop(-1))
				print("Evaluating: " + str(x) + " " + val + " " + str(y))
				stack.append(y-x)
			elif val == "*":
				#
				x = int(stack.pop(-1))
				y = int(stack.pop(-1))
				print("Evaluating: " + str(x) + " " + val + " " + str(y))
				stack.append(y*x)
			elif val == "/":
				#
				x = int(stack.pop(-1))
				y = int(stack.pop(-1))
				print("Evaluating: " + str(x) + " " + val + " " + str(y))
				stack.append(y/x)
			else:
				print("pushing " + val + " to stack")
				stack.append(val)
		print(stack[0])
		return stack[0]

test = Solution()
test.reversePolish(["2", "1", "+", "3", "*"])
test.reversePolish(["4", "13", "5", "/", "+"])