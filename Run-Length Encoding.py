"""
Intuition
One by one we traverse through values and count the appearance of the alphabet and accordingly add it to a string and return it.
"""
class Solution:
    def solve(self, s):
        temp = ""
        st = ""
        ct = 0
        for i in s:
            if temp == "":
                temp = i
                ct = 1
                continue
            if temp == i:
                ct += 1
            else:
                st += str(ct) + temp
                ct = 1
                temp = i
        st += str(ct) + temp
        return st