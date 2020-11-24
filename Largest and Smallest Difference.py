class Solution:
    def solve(self, nums, k):
        nums.sort()
        ls = []
        for i in range(len(nums) - k + 1):
            ls.append(nums[i + k - 1] - nums[i])
        return min(ls)