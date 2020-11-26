"""
Intuition
Here, we just compare the number with it's frequency using the Counter() function and return whether True or False.
"""
class Solution:
    def solve(self, nums):
        ct = Counter(nums)
        for i, j in ct.items():
            if i == j:
                return True
        return False