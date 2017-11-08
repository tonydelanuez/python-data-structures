def quicksort(arr, left, right):
	index = partition(arr, left, right)
	if left < (index - 1):
		quicksort(arr, left, index -1 )
	if index < right: 
		quicksort(arr, index, right)
	

def partition(arr, left, right):
	pivot = arr[(left + right) // 2]
	while left <= right:
		while (arr[left] < pivot):
			left += 1
		while (arr[right] > pivot): 
			right -= 1
		if (left <= right):
			swap(arr, left, right)
			left += 1
			right -= 1
	return left

def swap(arr, one, two):
	temp = arr[one]
	arr[one] = arr[two] 
	arr[two] = temp


nums = [67, 2, 14, 5, 9, 100, 67, 32, 19, 71, 99]
quicksort(nums, 0, len(nums) -1)
print(nums)