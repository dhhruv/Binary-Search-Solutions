class Solution:
    def solve(self, intervals):
        if len(intervals) == 1:
            return 0
        intervals.sort()
        ls = [intervals[0]]
        for i in range(1, len(intervals)):
            if ls[-1][1] >= intervals[i][0]:
                ls[-1][1] = max(ls[-1][1], intervals[i][1])
            else:
                ls.append(intervals[i])
        if len(ls) == 1:
            return 0
        return ls[-1][0] - ls[0][1]