"""
Intuition
Append 1 in back and front of every list and add all the consecutive numbers from the previous list and return as asked.
"""
class Solution:
    def solve(self, n):
        if n == 0:
            return [1]
        if n == 1:
            return [1, 1]
        ls = [1, 1]
        temp = [1, 1]
        for i in range(2, n + 1):
            ls = temp
            temp = [1]
            for i in range(len(ls) - 1):
                temp.append(ls[i] + ls[i + 1])
            temp.append(1)
        return temp