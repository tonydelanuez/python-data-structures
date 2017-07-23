"""
Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges. For example, given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”] 
Example Questions Candidate Might Ask: Q: What if the given array is empty? A: Then you should return [“0->99”] as those ranges are missing. Q: What if the given array contains all elements from the ranges? A: Return an empty list, which means no range is missing. 
"""




class Solution(object):
	def missingRanges(self, nums, start, end):
		#If the array is empty, return "0->99"
		print(nums)
		def arrowFormat(tup):
			if tup[0] == tup[1]:
				return tup[0]
			else: 
				return str(tup[0]) + "->" + str(tup[1])

		ranges = []
		# Handles our zero case
		last = start - 1
		for i in range(len(nums) + 1):
			
			current = (end + 1) if (i == len(nums)) else nums[i]
			if(current - last >= 2):
				ranges.append(arrowFormat((last + 1, current - 1)))
			# Make sure there's a difference of at least 2 before we append a new result
			last = current

		print(ranges)




test = Solution()
test.missingRanges([0], 0 , 99)
test.missingRanges([99], 0 , 99)
test.missingRanges([55], 0 , 99)
test.missingRanges([1], 0 , 99)
test.missingRanges([2,13], 0 , 99)
test.missingRanges([1,4,10,97], 0 , 99)
test.missingRanges([1,2,13,55,89], 0 , 99)
