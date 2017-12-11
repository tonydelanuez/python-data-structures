class Solution(object):
	def reverse(self, x):
		s = str(x)
		negative = False
		if s[0] == "-":
			negative = True
			s = s[1::]

		s = s[::-1]
		s = ("-"+s) if negative else s
		print(int(s))

test = Solution()
test.reverse(189)
test.reverse(100)
test.reverse(-501)
