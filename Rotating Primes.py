"""
Intuition
All rotations formed of the given number. Then check whether prime or not with O(sqrt(n)) time complexity and return accordingly.
"""
class Solution:
    def solve(self, n):
        def check(val):
            i = 2
            while i * i <= val:
                if val % i == 0:
                    return False
                i += 1
            return True

        ls = []
        s = str(n)
        for i in range(len(s)):
            ls.append(s[i:] + s[:i])
        ls = [int(i) for i in ls]

        for i in ls:
            if not check(i):
                return False
        return True