"""
Intuition
One by one we iterate and get the count.
eg: n=49
i=25 : ct=1,n=24
i=10 : ct=3,n=4
i=5 : ct=3,n=4
i=1 : ct=7,n=0
"""
class Solution:
    def solve(self, n):
        ct = 0
        for i in [25, 10, 5, 1]:
            if n >= i:
                ct += n // i
                n %= i
        return ct