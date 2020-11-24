class Solution:
    def solve(self, s, k):
        d = {}
        for i in range(len(s) - k + 1):
            d[s[i : i + k]] = d.get(s[i : i + k], 0) + 1
        return sum(1 for i, val in d.items() if val > 1)