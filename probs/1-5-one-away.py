"""
One Away: There are three types of edits that can be performed on the strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. 

EXAMPLE:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

"""


def one_away(s, t):
	# Get length of both strings
	m = len(s)
	n = len(t)
	# Iterate through the length of the smaller of the two strings
	for i in range(min(m, n)):
		# If the letters don't match, we need to shift the entire array
		if s[i] != t[i]:
			# Three cases. s is larger, s is smaller, s same size. 
			# Take the rest of the subarray of s if s is larger.
			# Take the rest of the subarray of t is t is larger.
			# DO NOT FORGET THE COLON. YOU MUST MAKE A SUBARRAY.  
			# Third case is covered by the >=, <=.  
			return s[i+(1 if m >= n else 0):] == t[i + (1 if m <= n else 0):]
	# If there are no mismatches (we don't return) but the difference in length isn't exactly one, we know there are extra characters at the end that break our size limits. 
	return abs(m - n) == 1





print(one_away("pale", "ple"))
print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
