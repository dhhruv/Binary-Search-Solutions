"""
Intuition
Simple condition to check whether the rectangles overlap or not.
"""
class Solution:
    def solve(self, rect0, rect1):
        if (rect0[2] > rect1[0] and rect0[3] > rect1[1]) and (
            rect1[2] > rect0[0] and rect1[3] > rect0[1]
        ):
            return True
        return False