class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create two pointers that progress through the list. If we find a duplicate, move left ptr to duplicate char 
        print("Finding longest substring with no repeating characters of " + str(s))
        position = {}
        if s == "":
            return 0

        longest = 0
        j = 0
        for i in range(len(s)):
            # Check if this is already a used character, find location
            if s[i] in position:
                j = max(j, position[s[i]] + 1)
            # Keep track of furthest along occurence of that value
            position[s[i]] = i
            # get width of makeshift buffer
            longest = max(longest, i - j + 1)
        print(longest)

test = Solution()
test.lengthOfLongestSubstring("aabcdeef")
test.lengthOfLongestSubstring("abc")
test.lengthOfLongestSubstring("")
test.lengthOfLongestSubstring("zxcqweqkj")
test.lengthOfLongestSubstring("herewego")