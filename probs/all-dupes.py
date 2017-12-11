nums = [4,3,2,7,8,2,3,1,4]

for i in nums: 
	if nums[abs(nums[i])] >= 0:
		nums[abs(nums[i])] = - nums[abs(nums[i])]
	else:
		print(abs(nums[i]))
