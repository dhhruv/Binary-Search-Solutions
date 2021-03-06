"""
Intuition
If any of the [start,end] in cut lies in the list of intervals then we carve and append the new interval in a list and return it.
"""
class Solution:
    def solve(self, intervals, cut):
        ls = []
        for i in intervals:
            if i[0] < cut[0] < i[1]:
                i[1] = cut[0]
                ls.append(i)
            elif i[0] < cut[1] < i[1]:
                i[0] = cut[1]
                ls.append(i)
            elif i[0] >= cut[0] and i[1] <= cut[1]:
                pass
            else:
                ls.append(i)
        return ls