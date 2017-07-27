class Solution(object):
	def addTwoNums(self, l1, l2):
		l1 = l1.reverse()
		l2 = l2.reverse()
		p1 = 0
		p2 = 0
		result = []
		carry = 0
		while(p1 < len(l1)) and (p2 < len(l2)):
			local_sum = l1[p1] + l2[p2] + carry
			result.append(local_sum)
			carry = 1 if (local_sum > 9) else 0
			p1 += 1
			p2 += 1
		if(p1 < len(l1)):
			result.extend(l1)
		elif(p2 < len(l2)):
			result.extend(l2)

		print(result)
		return result



test = Solution()
l1 = [2, 4, 3]
l2 = [5, 6, 4]
test.addTwoNums()