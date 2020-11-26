"""
Intuition
One by one we add n in set if not identified. After that we add (all digits of n ** 2) and recheck until loop is formed or n==1.
"""
class Solution:
    def solve(self, n):
        s = set()
        while n != 1:
            if n in s:
                return False
            else:
                s.add(n)
            val = n
            n = 0
            while val > 0:
                n += (val % 10) ** 2
                val //= 10
        return True