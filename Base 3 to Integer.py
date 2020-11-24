"""
Intuition
Traditional method/way to find the decimal from ternary.
"""
class Solution:
    def solve(self, s):
        return sum(int(s[i]) * 3 ** (len(s) - i - 1) for i in range(len(s)))