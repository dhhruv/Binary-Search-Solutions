"""
Intuition
As asked in the problem we set different functions on different count values and return the string made at the given value.
"""
class Solution:
    def solve(self, n):
        s = "xxy"
        ct = 0
        for i in range(1, n + 1):
            if ct == 0:
                s = s * 2
            elif ct == 1:
                s = s[::-1]
            elif ct == 2:
                temp = ""
                for j in s:
                    if j == "x":
                        temp += "y"
                    else:
                        temp += "x"
                s = temp
            if ct == 2:
                ct = 0
            else:
                ct += 1
        return s