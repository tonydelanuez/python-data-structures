"""
Write a method to replace all spaces in a string with "%20"
You may assume that the string has sufficient space at the end to hold additional characters, and that you are given the true length of th string. 

EXAMPLE: 
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""
def urlify(s, true_length):
	return s.replace(" ", "%20")

print urlify("Mr John Smith", 13)

