def binary_search_recursive(x, arr, low, high):
	if low > high: return -1
	mid = (low + high) // 2
	if x > arr[mid]:
		return binary_search_recursive(x, arr, mid + 1, high)
	elif x < arr[mid]:
		return binary_search_recursive(x, arr, low, high -1)
	else:
		return mid

def do_binary_search_recursive(x, arr):
	return binary_search_recursive(x, arr, 0, len(arr) - 1)

a = [1, 2, 4, 6, 8, 10 , 12]
print(do_binary_search_recursive(1, a)) 
print(do_binary_search_recursive(2, a))
print(do_binary_search_recursive(4 ,a))
print(do_binary_search_recursive(6, a))
print(do_binary_search_recursive(8, a))
print(do_binary_search_recursive(10, a))
print(do_binary_search_recursive(12, a))
print(do_binary_search_recursive(0, a))