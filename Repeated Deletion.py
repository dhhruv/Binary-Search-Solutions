"""
Intuition
Here, we use a stack to solve the problem. If new character occurs we check whether it is on our top of the stack or not, if yes then we pop it. Else if previous character is the same as new character then no need to pop as it is already popped and if neither occurs then append the new(distinct) character.
"""
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