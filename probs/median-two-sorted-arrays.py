def findMedianSortedArrays(nums1, nums2):
	merged = []
	p1 = 0
	p2 = 0
	# Merge the two lists
	while(p1 < (len(nums1))) and (p2 < (len(nums2))):
		print("Comparing " + str(nums1[p1]) + " and " + str(nums2[p2]))
		if nums1[p1] < nums2[p2]:
			merged.append(nums1[p1])
			p1 +=1
		else:
			merged.append(nums2[p2])
			p2 += 1
	if(p1 < (len(nums1))):
		merged.extend(nums1[p1::])
	else:
		merged.extend(nums2[p2::])
	print("merged checks: ")
	print(nums1[p1::])
	print(nums2[p2::])
	if len(merged) == 1:
		return merged[0]
	print("MERGED --")
	print(merged)
	middle = [len(merged) // 2] if (len(merged) % 2 == 1) else [len(merged)//2 -1, len(merged)//2 ]
	print("MIDDLE --")
	print(middle)
	sum_nums = 0
	for x in middle:
		print(x)
		sum_nums += merged[x]
	print("Sum: ", sum_nums)
	return (1.0*sum_nums/len(middle))

if __name__ == '__main__':
	n1 = [1,2]
	n2 = [3,4]
	print(findMedianSortedArrays(n1, n2))
