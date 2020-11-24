"""
Intuition
We keep the indexes to be removed by appending them in a list and then remove them using pop in the end.
"""
class Solution:
    def solve(self, fighters, bosses):
        n = fighters.count(1)
        temp = []
        for i in range(len(bosses)):
            if bosses[i].count(1) < n:
                temp.append(i)
        a = 0
        for i in temp:
            bosses.pop(i - a)
            a += 1
        return bosses