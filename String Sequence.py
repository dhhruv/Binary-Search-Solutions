"""
Intuition:
Here one by one as asked in the problem, we append value in the list and return the last element of the list..
"""
class Solution:
    def solve(self, s0, s1, n):
        if n == 0:
            return s0
        if n == 1:
            return s1
        ls = [s0, s1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                ls.append(ls[i - 1] + ls[i - 2])
            else:
                ls.append(ls[i - 2] + ls[i - 1])
        return ls[-1]