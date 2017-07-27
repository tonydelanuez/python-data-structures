# Roman to Integer
# Given a roman numeral, convert it to an integer

# Input is guaranteed to be within the range from 1 to 3999. 

class Solution(object):
	def romanToInt(self,s):
		print("Converting " + s + " to integer")

		values = {
		"M": 1000, "D": 500,
		"C": 100, "L": 50,
		"X": 10, "V": 5,
		"I":1
		}

		previous = 0
		total = 0
		for index, val in enumerate(s):
			current = values[val]
			# Would have to sacrifice by 2 * previous since current was already added. 
			total += (current - 2 * previous) if (current > previous) else current
			previous = current

		print(total)

test = Solution()
test.romanToInt("XV")
test.romanToInt("XXXVI")
test.romanToInt("MMXII")
test.romanToInt("MCMXCVI")
