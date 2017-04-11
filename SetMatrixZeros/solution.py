# https://leetcode.com/problems/set-matrix-zeroes/#/description

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        changes = set()
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] is 0:
                    for x_1 in range(len(matrix[y])):
                        changes.add((x_1, y))
                    for y_1 in range(len(matrix)):
                        changes.add((x, y_1))

        for change in changes:
            matrix[change[1]][change[0]] = 0
