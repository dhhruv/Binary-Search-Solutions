"""
Intuition
One by one we iterate and use k=A[k] and check the conditions whether a loop is formed or return the total jumps we made.
"""
class Solution:
    def solve(self, A, k):
        if A == []:
            return 0
        s = set()
        while True:
            if k >= len(A):
                break
            k = A[k]
            if k >= len(A):
                break
            if k in s:
                return -1
            s.add(k)
        return len(s) + 1