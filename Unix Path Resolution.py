"""
Intuition
If ".." then pop() values from the list else append values till the end of traversal.
"""
class Solution:
    def solve(self, path):
        ls = []
        for i in path:
            if i == "..":
                if len(ls) != 0:
                    ls.pop()
            elif i == ".":
                pass
            else:
                ls.append(i)
        return ls