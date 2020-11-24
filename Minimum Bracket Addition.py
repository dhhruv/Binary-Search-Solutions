"""
Intuition
Here we check the open and closed brackets. If open occurs then increment c1 then if closing bracket occurs then we check whether there is any open bracket, if Yes then we decrement c1 else we increment c2.
"""
class Solution:
    def solve(self, s):
        c1 = 0
        c2 = 0
        for i in s:
            if i == "(":
                c1 += 1
            else:
                if c1 > 0:
                    c1 -= 1
                else:
                    c2 += 1
        return c1 + c2