"""
Intuition
Here, we use dictionary to make the work easier. A Counter() can also be used to make it easy. Just count the slices of k-length slices in the string s and return the sum of slices appearing more than once.
"""
class Solution:
    def solve(self, s, k):
        d = {}
        for i in range(len(s) - k + 1):
            d[s[i : i + k]] = d.get(s[i : i + k], 0) + 1
        return sum(1 for i, val in d.items() if val > 1)