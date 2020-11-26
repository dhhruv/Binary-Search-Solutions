"""
Intuition
To change from odd to even or from even to odd, we add 1 to the sequence and to iterate through either odd or even we add 2 for the following range of count.
"""
class Solution:
    def solve(self, n):
        ls = [1]
        ct = 1
        while len(ls) <= n:
            ls.append(ls[-1] + 1)
            for i in range(ct):
                ls.append(ls[-1] + 2)
            ct += 1
        return ls[n]