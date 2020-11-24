"""
Intuition
Here, we just add the elements in a set and check whether the length is the same as n or not. If the element is not in the set then it'll have now friends.
"""
class Solution:
    def solve(self, n, friends):
        s = set()
        for i, j in friends:
            s.add(i)
            s.add(j)
        return len(s) == n