"""
Given an array, find the length of smallest subarray such that when that subarray is sorted, the rest of the array is sorted. 
"""

def min_subarray_sorted(arr):
	# i = 0 
	# j = len(arr) - 2
	# while(i < (len(arr) -1) and (arr[i] > arr[i+1])):
	# 	i += 1
	# while(j > 0) and (arr[j] < arr[j+1]):
	# 	j -= 1
	# return j-i
	max_ind = arr.index(max(arr))
	min_ind = arr.index(min(arr))
	end_arr = len(arr) -1
	return (end_arr - max_ind) + (min_ind - 1) + (max_ind - min_ind) 


test = [1, 2, 3, 17, 9, 8, 4, 5, 80, 64, 13, 22, 50]
test = [1, 4, 2, 3, 5]
test = [3, 1, 5, 6, 7]

print(min_subarray_sorted(test))


