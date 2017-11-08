def binary_search(val, arr):
	low = 1
	high = len(arr) - 1
	while(low < high):
		mid = (low + high)//2
		mid_val = arr[mid]
		if val == arr[mid]:
			return True
		elif val > mid_val:
			low = mid + 1
		else:
			high = mid - 1
	return False


myarr = [1, 2, 3, 4, 5]
print(binary_search(3, myarr))
print(binary_search(7, myarr))

