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

		def afterDec(i, num):
			if((i + 1 > len(num) -1) or isASCIINum(num[index+1])):
				return False
			else:
				return True

		print("Trying string: " + str(s))
		if s == "":
			return False

		first = s[0]
		if isASCII(first) or first == "-":
			exponents = 0
			decimals = 0
			print(str(s) + " starts with a number")
			for index, val in enumerate(s[1::]):
				if (val == "e") and ((index + 1 <= len(s)-1) and isASCII(s[index])) and (exponents < 1):
					exponents += 1
					print(isASCII(s[index+1]))
					print("found exponent")
				elif (val == "." and decimals < 1):
					decimals += 1
					print("Found decimal")
				elif not isASCII(val):
					print(val)
					print("Decimals: " + str(decimals))
					print("Exponents: " + str(exponents))
					print("Nope. Not a number")
					return False
			print(str(s) + " is a number!")

		elif first is '.':
			print(str(s) + " starts with a decimal point")
			if(len(s) == 1):
				print("This is only a decimal!")
				return False
			for val in s[1::]:
				if not isASCII(val):
					print("Not a valid decimal.")
					return False
			print(str(s) + " is a number!")
			return True
		else:
			print(str(s) + " is not a numerical value")
			return False

test = Solution()
# test.isNumber("7")
# test.isNumber("A")
# test.isNumber(".5")
# test.isNumber("1s")
# test.isNumber("1e10")
# test.isNumber("1a10")
test.isNumber(" .1")
test.isNumber("-1.")
test.isNumber("2e0")