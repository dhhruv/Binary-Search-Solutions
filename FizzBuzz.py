"""
Intuition
As asked in the problem we first check for n % (15,3,5) in the order for all i till n and return the list.
"""
class Solution:
    def solve(self, n):
        ls = []
        st = ""
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                st = "FizzBuzz"
            elif i % 3 == 0:
                st = "Fizz"
            elif i % 5 == 0:
                st = "Buzz"
            else:
                st = str(i)
            ls.append(st)
        return ls