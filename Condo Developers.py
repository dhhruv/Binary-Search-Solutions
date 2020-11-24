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