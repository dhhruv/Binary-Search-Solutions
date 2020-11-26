"""
Intuition
Even + Odd = Odd
Using this condition, here I make combinations and generalize them to a formula.
"""
class Solution:
    def solve(self, nums):
        e = [i for i in nums if i % 2 == 0]
        return (len(nums) - len(e)) * len(e)