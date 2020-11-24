"""
Intuition
Traverse through all values and check whether same then append if different then pop values and return the length.
"""
class Solution:
    def solve(self, s):
        ls = []
        for i in s:
            if len(ls) == 0:
                ls.append(i)
            elif ls[-1] == i:
                ls.append(i)
            else:
                ls.pop()
        return len(ls)