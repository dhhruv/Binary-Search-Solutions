"""
Intuition
First of all we sort according to the end time of intervals and then one by one check whether overlapping is happening and accordingly return the count.
"""
class Solution:
    def solve(self, intervals):
        ct = 0
        intervals = sorted(intervals, key=lambda x: x[1])
        e = intervals[0][1]
        for i in range(1, len(intervals)):
            if e <= intervals[i][0]:
                e = intervals[i][1]
                ct += 1
        return len(intervals) - ct - 1