class Solution:
    def solve(self, words):
        ct = dict()
        for i in words:
            temp = "".join(sorted(i))
            ct[temp] = ct.get(temp, 0) + 1
        return max(ct.values())