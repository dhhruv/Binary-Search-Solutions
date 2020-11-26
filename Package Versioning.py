"""
Intuition
Here, we use a flag to check whether any other bigger value has occurred while traversing or not. If yes then True and if not then return False.
"""

class Solution:
    def solve(self, older, newer):
        if older == newer:
            return False
        lo = older.split(".")
        ln = newer.split(".")
        f = False
        for i, j in zip(lo, ln):
            if int(i) < int(j):
                f = True
            if int(i) > int(j) and f == False:
                return False
        return True