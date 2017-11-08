def merge(arr1, arr2):
	print("Array 1: ", arr1)
	print("Array 2: ", arr2)
	result = []
	p1 = p2 = 0
	print("Doing the merge...")
	while(p1 < len(arr1) and p2 < len(arr2)):
		print("Array1: ", arr1[p1:])
		print("Array2: ", arr2[p2:])
		print("Result: ", result)
		print("Comparing " + str(arr1[p1]) + " and " + str(arr2[p2]))
		if(arr1[p1] <= arr2[p2]):
			print("Thing at p1 smaller, adding to result")
			result.append(arr1[p1])
			p1 += 1
			print(result)
		else: 
			print("Thing at p2 smaller, adding to result")
			result.append(arr2[p2])
			p2 += 1
			print(result)
	if(p1 < len(arr1)):
		print("Still have elements left in array 1. Dumping array 1")
		result = result + arr1
	if(p2 < len(arr2)):
		print("Still have elements left in array 2. Dumping array 2")
		result = result + arr2
	return result

a1 = [1, 3, 5]
a2 = [2, 4, 7, 9, 19, 20]

print(merge(a1, a2))