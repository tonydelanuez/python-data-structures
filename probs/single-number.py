class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		the_num = 0
		for val in nums:
			the_num = the_num ^ val
			print(the_num)
		print(the_num)
		return(the_num)

test = Solution()
numbers = [1,1,2,2,3,3,4,5,5,6,6,7,7]

test.singleNumber(numbers)