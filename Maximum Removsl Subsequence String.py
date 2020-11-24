class Solution:
    def solve(self, s, t):
        l = []
        r = []
        c1 = -1
        c2 = -1
        c3 = -1
        j = 0
        for i in range(len(s)):
            if s[i] == t[j]:
                l.append(i)
                j += 1
            if j == len(t):
                c1 = len(s) - i - 1
                break
        j = len(t) - 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == t[j]:
                r.insert(0, i)
                j -= 1
            if j == -1:
                c2 = i
                break
        for i in range(len(t) - 1):
            c3 = max(c3, r[i + 1] - l[i] - 1)
        return max(c1, c2, c3)