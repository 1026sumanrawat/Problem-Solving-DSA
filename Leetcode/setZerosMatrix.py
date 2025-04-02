class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        traveled = set()
        def dfs(r, c):
            traveled.add((r,c)) 
            for j in range(len(matrix[0])):
                if matrix[r][j] != 0:
                    matrix[r][j] = 0
                    traveled.add((r,j))
                if (r,j) not in traveled and matrix[r][j] == 0:
                    continue
            for i in range(n):
                if matrix[i][c] != 0:
                    matrix[i][c] = 0
                    traveled.add((i,c))
                if (i,c) not in traveled and matrix[i][c] == 0:
                    continue
            return   
        for i in range(n):
            for j in range(m):
                if (i,j) not in traveled and matrix[i][j] == 0:
                    dfs(i,j)
        return matrix
