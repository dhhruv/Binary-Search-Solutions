"""
Intuition
If p>20 then,
Rate of degradation r=t/(100-p)
Last long r till p>20 then 2*r for [0,20] then add both.

if p<=20 then:
Rate of degradation r=t/(80+(2*(20-p)))
Because the battery drains 2 times slower so you've to add this in rate of degradation.
So last long till 2*r.
"""
class Solution:
    def solve(self, t, p):
        if p > 20:
            return (t / (100 - p)) * (p - 20) + (2 * (t / (100 - p))) * 20
        else:
            return (t / (80 + 2 * (20 - p))) * p * 2