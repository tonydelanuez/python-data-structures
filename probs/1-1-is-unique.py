"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structure?

"""

def all_unique_extra_space(s):
	characters = []
	for i in s:
		if i in characters:
			return False
		characters.append(i)
	return True

def all_unique_no_extra(s):
	s = sorted(s)
	tmp = None
	for i in s: 
		if tmp == i:
			return False
		tmp = i
	return True

print(all_unique_no_extra("ssam"))
print(all_unique_no_extra("mark"))
