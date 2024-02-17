# 1. Two Sum
# Solved
# Easy
# Topics
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 10**4
# -10**9 <= nums[i] <= 10**9
# -10**9 <= target <= 10**9
# Only one valid answer exists.
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
class Solution:
    def twoSum(self, nums, target):
        lengh = len(nums)
        for element in nums:
            if element < -10 ** 9 or element > 10 ** 9:
                return None
        if target >= -10 ** 9 and target <= 10 ** 9 and lengh >= 2 and lengh <= 10 ** 4:
            for i in range(lengh):
                for j in range(i + 1, lengh):
                    if nums[i] + nums[j] == target:
                        return [i, j]


new_object = Solution()
nums = [0, 4, 3, 0]
target = 0
print(new_object.twoSum(nums, target))

