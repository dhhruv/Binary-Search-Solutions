class Solution:
    def solve(self, s):
        ls = [""]
        prev = ""
        for i in s:
            if i == ls[-1]:
                ls.pop()
            elif prev == i:
                pass
            else:
                ls.append(i)
            prev = i
        return "".join(ls)