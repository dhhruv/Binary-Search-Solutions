"""
Intuition
First of all we find the ASCII value for all alphabets than add k and use (%26) to make in the range of [0,25] and then add 97 to get the ASCII value and return the string.
"""
class Solution:
    def solve(self, s, k):
        return "".join([chr((ord(i) + k - 97) % 26 + 97) for i in s])