# Zipping two lists together, making a comparison at each index.
# If you select from one list, increment its pointer. 
def merge(num_1, num_2):
		p1 = p2 = 0
		result = []
		while p1 < len(num_1) and p2 < len(num_2):
			if(num_1[p1] > num_2[p2]):
				result.append(num_2[p2])
				p2 += 1
			else:
				result.append(num_1[p1])
				p1 +=1
		result += num_1[p1:]
		result += num_2[p2:]
		return result

# Main method to run. Once we split down to length 1 we reach our base case
def merge_sort(nums):
	if(len(nums) <= 1):
		return nums
	middle = int(len(nums)/2)
	list_1 = merge_sort(nums[:middle])
	list_2 = merge_sort(nums[middle:])
	return merge(list_1, list_2)

if __name__ == '__main__':
	print(merge_sort([3,17,8,4,9,10,2,5,1,0]))