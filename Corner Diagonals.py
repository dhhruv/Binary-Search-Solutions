"""
Intuition
For even n there are 2n diagonals and for odd there are 2n-1 diagonals so accordingly values are returned.
"""
class Solution:
    def solve(self, n):
        if n % 2 == 0:
            return (n ** 2) - (2 * n)
        return (n ** 2) - (2 * n - 1)