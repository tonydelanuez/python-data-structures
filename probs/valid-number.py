"""

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one
"""

class Solution(object):
	def isNumber(self, s):
		# Remove leading and trailing whitespace
		s = s.strip()
		# Check if all characters are in ASCII ranges 
		# In order to get the ASCII value of a character, we use ord(character) 

		# Make sure that string either starts with number or . 
		def isASCII(n):
			return 48 <= ord(n) <= 57

		print("Trying string: " + str(s))
		if s == "":
			return False

		first = s[0]
		if isASCII(first):
			exponents = 0
			print(str(s) + " starts with a number")
			for index, val in enumerate(s):
				if (val == "e") and (isASCII(s[index+1])) and (exponents < 1):
					exponents += 1
					print(isASCII(s[index+1]))
					print("found exponent")
				elif not isASCII(val):
					print("Nope. Not a number")
					return False
			print(str(s) + " is a number!")

		elif first is '.':
			print(str(s) + " starts with a decimal point")
			for val in s[1::]:
				if not isASCII(val):
					print("Not a valid decimal.")
					return False
			print(str(s) + " is a number!")

		else:
			print(str(s) + " is not a numerical value")


test = Solution()
test.isNumber("7")
test.isNumber("A")
test.isNumber(".5")
test.isNumber("1s")
test.isNumber("1e10")
test.isNumber("1a10")