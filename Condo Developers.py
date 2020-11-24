"""
Intuition
First we find maximum in all rows and columns. Then one by one we traverse and check whether the value is equal to it's maximum value in row/column or not. If not then assign the maximum value of that row else the maximum value of the column if it goes far the maximum value of it's row.
"""
class Solution:
    def solve(self, matrix):
        r = [max(i) for i in matrix]
        c = [max(i) for i in zip(*matrix)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if r[i] < c[j]:
                    matrix[i][j] = r[i]
                else:
                    matrix[i][j] = c[j]
        return matrix