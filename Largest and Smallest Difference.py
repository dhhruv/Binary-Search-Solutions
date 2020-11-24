"""
Intuition
Here, we calculate all the differences for the i-th and (i+k-1)th values after sorting nums and return the minimum value from the list.
"""
class Solution:
    def solve(self, nums, k):
        nums.sort()
        ls = []
        for i in range(len(nums) - k + 1):
            ls.append(nums[i + k - 1] - nums[i])
        return min(ls)