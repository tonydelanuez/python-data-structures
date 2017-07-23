class Solution(object):
	def isPalindrome(self, s):
        if str(s) == '':
            return False
        
        s = s.lower()
        counts = {}
        for i in s:
            if i in counts:
                count = counts[i] + 1
                counts[i] = 1
            else:
                counts[i] = 1
        uniques = 0
        for x in counts:
            if (counts[x] % 2) != 1:
                uniques += 1
        if uniques not in (0,1) or uniques == len(s):
        	print( s + "is not a palindrome")
            return False
        else:
        	print( s +_ "is a palindrome!")
            return True


			

test = Solution()
test.isPalindrome("Darn")
test.isPalindrome("racecar")
test.isPalindrome("aa")