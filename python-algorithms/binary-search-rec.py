# Start with the middle element. If the element we are searching for is found, return. 
# If we do not find the element, recursively call on the left or right sublists (relative to middle)
# Critical Notes: The list must be sorted already in order to get a correct result for binary search.
# Binary search space complexity: O(1)
# Binary search time complexity: O(logn)
def binary_search_recursive(alist, item):
	if len(alist) is 0: 
		return False
	else:
		# Must use floor division to avoid float error
		middle = len(alist)//2
		if alist[middle] == item:
			return True
		else:
			if item < alist[middle]:
				# Darn, the item is too small. Go look for it on the left side. 
				return binary_search_recursive(alist[:middle], item)
			else: 
				# Too big! Go look for it on the right side
				return binary_search_recursive(alist[middle+1:], item)


def binary_search_iterative(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found: 
		middle = (first + last)//2

		if item == alist[middle]:
			#Found the item, we can stop.
			found =  True
		else:
			if item < alist[middle]:
				last = middle - 1
			else:
				first = middle + 1
	return found


test = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print("Testing recursive... Should be False then True.")
print(binary_search_recursive(test, 9))
print(binary_search_recursive(test, 13))
print("Testing iterative... Should be False then True.")
print(binary_search_iterative(test, 9))
print(binary_search_iterative(test, 13))