"""
Intuition
Here, first of all we merge all the lists that have common in a union and then we check the maximum range for the intervals from the new list.
"""
class Solution:
    def solve(self, intervals):
        intervals.sort()
        ls = [intervals[0]]
        for i in range(1, len(intervals)):
            if ls[-1][1] >= intervals[i][0]:
                ls[-1][1] = max(ls[-1][1], intervals[i][1])
            else:
                ls.append(intervals[i])
        return max(i[1] - i[0] + 1 for i in ls)