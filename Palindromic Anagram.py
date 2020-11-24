"""
Intuition
Here we use the Counter() to check whether string is palindrome or not. If count of the alphabet is odd viz. 'e' in "racecar" then there should be only one alphabet that can be odd. If all counts are even then it can be used to from a palindrome.
"""
class Solution:
    def solve(self, s):
        ct = 0
        count = Counter(s)
        for i, val in count.items():
            if val % 2 != 0:
                ct += 1
        return ct == 0 or ct == 1