"""
Intuition
Here, I go to every intersection's first and last limit and check the necessary conditions like < and > respectively and return the value.
"""
class Solution:
    def solve(self, intervals):
        l = intervals[0][0]
        h = intervals[0][1]
        for i in intervals:
            if l < i[0]:
                l = i[0]
            if h > i[1]:
                h = i[1]
        return [l, h]