"""
Intuition
Here, I make every rotation of the string and add them to set. So whenever another rotation occurs then the set will identify and count will not be incremented.
"""
class Solution:
    def solve(self, words):
        s = set()
        ct = 0

        for i in words:
            if i not in s:
                ct += 1
            for j in range(len(i)):
                s.add(i[j:] + i[:j])
        return ct