"""
Find the contiguous subarray within an array (containing at least one number) that has the largest sum. 

For example, given the array [2,1,-3,4,-1,2,1,-5,4]
The contiguous array [-4, -1, 2, 1] has the largest sum = 6

"""

class Solution(object):
	def maximumSubarray(self, arr):
		print(str(arr))
		# Keep track of local and global maxima
		max_here = arr[0]
		max_so_far = arr[0] 
		# Iterate through for rest of the array
		for i in range(1,len(arr)):
			# If the current element is larger than the value you would get by adding it and the cached max, take the current element instead. 
			max_here = max(max_here + arr[i], arr[i])
			# Global max is checked at every state against local max.
			max_so_far = max(max_here, max_so_far)
		print(max_so_far)

test = Solution()
array = [2,1,-3,4,-1,2,1,-5,4]
test.maximumSubarray(array)

