class Solution(object):
	def integerToRoman(self, x):
		print("Creating a roman numeral representation of " + str(x) + "...")
		# Keep the values and symbols separate for easy iteration. 
		values = [
		1000, 900, 500, 400,
		100, 90, 50, 40,
		10, 9, 5, 4,
		1
		]
		symbols = [
		"M", "CM", "D", "CD",
		"C", "XC", "L", "XL",
		"X", "IX", "V", "IV",
		"I"
		]
		roman = ""
		it = 0
		print("Let's get this started.")
		while(x > 0):
			print("Dividing by " + str(values[it]) + "...")
			# Get the amount of occurrences for each digit
			leftover = x // values[it]
			print("Found " + str(leftover) + " occurrences")
			for j in range(leftover):
				print("Appending " + symbols[it])
				roman += symbols[it]
				x -= values[it]
			it += 1

		print("Done!")
		print(roman)



test = Solution()
test.integerToRoman(4562)
