"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

THE INPUT IS NOW SORTED. 

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# If the input array is sorted, we can search for the other element using a binary search 
# This improves our space complexity O(1) but bumps up the time to O(nlogn)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(arr, key, start):
            left = start
            right = len(arr) - 1
            while left < right: 
                middle = (left + right) // 2
                if arr[middle] < key:
                    left = middle + 1
                else: 
                    right = middle
            return  left if (left == right and arr[left] == key) else -1

                    
        print("At start of solution")
        print("Looking for indexes in array where two numbers add up to: " + str(target))
        print(nums)
        chk_map = {}
        for index, val in enumerate(nums):
            compl = target - val
            b_index = binarySearch(nums, compl, index+1)
            if b_index != -1:
                print([index , b_index ])
                print("Index " + str(index) + ": " + str(nums[index]) + " Index " + str(b_index) + ": " + str(nums[b_index]) + " add up to " + str(target))
                return

        print("didnt work out..")
        return False

        


        

nums = [2, 7, 11, 15]
target = 9
# Given the target number and a number we're currently on, we want to find index of target - num
attempt = Solution()
attempt.twoSum(nums, target)
