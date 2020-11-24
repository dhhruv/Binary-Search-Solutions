"""
Intuition
First of all I created a list of string of numbers from 1 to n and then sorted it will give me in lexicographic manner and then return the list as integers.
"""
class Solution:
    def solve(self, n):
        ls = [str(i) for i in range(1, n + 1)]
        ls.sort()
        ls = [int(i) for i in ls]
        return ls