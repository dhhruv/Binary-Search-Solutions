"""
Intuition
Here we use two pointers where i starts from front and j starts from the end after sorting the weights. If the sum of values at the pointers is <=limit then we can send the rocket and if the limit exceeds then we have only one option left that is to send weights[j] single in the rocket and repeat the same procedure.
"""
class Solution:
    def solve(self, weights, limit):
        weights.sort()
        i = 0
        j = len(weights) - 1
        ct = 0
        while i <= j:
            if weights[i] + weights[j] <= limit:
                ct += 1
                i += 1
                j -= 1
            else:
                ct += 1
                j -= 1
        return ct