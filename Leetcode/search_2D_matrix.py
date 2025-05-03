class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
                return False
        row = 0
        while row < len(matrix):
            if target == matrix[row][0]:
                return True
            if target < matrix[row][0]:
                break
            row += 1
        row = row - 1
        for j in range(len(matrix[0])):
            if target == matrix[row][j]:
                return True
        return False
