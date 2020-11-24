"""
Intuition
First of all we add all the possible sum of the lists in a new list and then return the maximum common sum of elements found in all the stacks using functools.
"""
class Solution:
    def solve(self, stacks):
        if len(stacks) == 0:
            return 0
        ls = []
        temp = []
        for i in stacks:
            temp = [0]
            val = 0
            for j in i:
                val += j
                temp.append(val)
            ls.append(temp)
        ans = list(reduce(lambda i, j: i & j, (set(x) for x in ls)))
        return max(ans)