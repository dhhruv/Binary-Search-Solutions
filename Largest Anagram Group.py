"""
Intuition
Here, we used dictionary to store the Count of the anagrams. We check the count of each word by sorting it and increasing it's count and returning it's maximum count.
"""
class Solution:
    def solve(self, words):
        ct = dict()
        for i in words:
            temp = "".join(sorted(i))
            ct[temp] = ct.get(temp, 0) + 1
        return max(ct.values())