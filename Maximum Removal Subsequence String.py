"""
Intuition
Here, there are 3 cases and we find the maximum output from the cases and return that.

First is the length of the leftover string s after string t has occurred from the front.
Then the length of the string s after string t has occurred from the end.
At last, the in-between length between two consecutive alphabets where one index occurs from left and another index occurs from right.
Maximum of any of the three cases is returned.
"""
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