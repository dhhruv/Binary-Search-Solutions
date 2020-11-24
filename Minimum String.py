class Solution:
    def solve(self, s, t):
        c1 = Counter(s)
        c2 = Counter(t)
        ct = 0
        for i, val in c2.items():
            ct += max(val - c1.get(i, 0), 0)
        return ct