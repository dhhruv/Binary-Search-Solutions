"""
Intuition
First of all we sort it and then we just check the (nums//2-1)th and (nums//2)th value and return it's value of difference. This is the simplest approach we can use.
"""
class Solution:
    def solve(self, nums):
        nums.sort()
        return nums[len(nums) // 2] - nums[(len(nums) // 2 - 1)]