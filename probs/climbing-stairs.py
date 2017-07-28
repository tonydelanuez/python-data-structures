class Solution(object):
	def climbStairs(self, n):
		# Establish base cases
		p = 1
		q = 1
		# Repeat for all steps
		for i in range(2,n+1):
			temp = q
			q += p
			p = temp
		print(q)
		return q

test = Solution()
test.climbStairs(4)