"""
Given a string, write a function to check if it a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. 

"""

def palindrome_permutation(s):
	s = s.lower()
	s = s.replace(" ", "")
	counts = {}
	for i in s: 
		if i in counts:
			counts[i] += 1
		else:
			counts[i] = 1
	print(counts)
	return (1 >= len([x for x in counts if ((counts[x] % 2) == 1)]))

print(palindrome_permutation("Tact Coa"))
print(palindrome_permutation("i am idiot"))