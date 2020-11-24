"""
Intuition
If count of odd values are found even then divide by 2 gives the answer and if odd count found then there is no way to solve all so -1.
"""
class Solution:
    def solve(self, nums):
        odd = 0
        for i in nums:
            if i % 2 == 1:
                odd += 1
        if odd % 2 == 1:
            return -1
        return odd // 2