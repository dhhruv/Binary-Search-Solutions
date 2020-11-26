"""
Intuition
First of all we add all the squares of a number in the set and then check whether (i x i) + (j x j) exists in the set or not.
"""
class Solution:
    def solve(self, nums):
        st = set(i * i for i in nums)
        for i in nums:
            for j in nums:
                if (i * i + j * j) in st:
                    return True
        return False