"""
One Away: There are three types of edits that can be performed on the strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. 

EXAMPLE:
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

"""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def one_away(s, t):
	print("Comparing words: " + str(s) + " and " + str(t))
	m = len(s)
	n = len(t)
	# If a character is not the same, apply an offset and check the rest of the array
	for i in range(min(m, n)):
		if s[i] != t[i]:
			# Compute the offset for the next index
			return s[i + (1 if m >= n else 0):] == t[i + (1 if m <= n else 0):]
	# Check the tail character(s)
	return abs(m - n) == 1 

print(one_away("pale", "ple"))
print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
