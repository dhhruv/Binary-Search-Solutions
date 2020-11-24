"""
Intuition
We make a set of all alphabets and simply check whether all are present in string s or not.
"""
class Solution:
    def solve(self, s):
        ct = set(list("qwertyuiopasdfghjklzxcvbnm"))
        return not [i for i in ct if i not in s.lower()]