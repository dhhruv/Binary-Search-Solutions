"""
Intuition
We add and pop values as given in the explanation until len(nums)!=1 and then return the new squeezed list formed.
"""
class Solution:
    def solve(self, nums):
        temp = nums.copy()
        ls = [temp]
        while len(nums) != 1:
            if len(nums) > 2:
                nums[1] += nums[0]
                nums.pop(0)
                nums[-2] += nums[-1]
                nums.pop()
                temp = list(nums)
                ls.append(temp)
                continue
            nums[1] += nums[0]
            nums.pop(0)
            temp = list(nums)
            ls.append(temp)
        return ls