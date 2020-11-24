"""
Intuition
One by one we add all the numbers till sum always remains positive and then add them to ma and return them.
"""
class Solution:
    def solve(self, nums):
        if len(nums) == 1:
            return nums[0]
        ma = 0
        s = 0
        for i in nums:
            s = max(s + i, 0)
            ma = max(ma, s)
        return ma