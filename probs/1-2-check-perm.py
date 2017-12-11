"""
Given two string, write a method to decide if one is a permutation of the other

"""
def check_permutation(s1, s2):
	s1 = s1.lower()
	s2 = s2.lower()
	print("Checking strings " + s1 + " & " + s2)

	if len(s1) != len(s2):
		return False
	sum_1 = 0
	sum_2 = 0
	for i in s1:
		sum_1 += ord(i)
	for j in s2:
		sum_2 += ord(j)
	if sum_1 == sum_2:
		return True
	return False

print(check_permutation("hello", "lohel"))
print(check_permutation("hello", "ifasj"))
print(check_permutation("", " "))
