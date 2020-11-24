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