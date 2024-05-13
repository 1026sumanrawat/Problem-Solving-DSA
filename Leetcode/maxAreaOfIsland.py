# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        path = set()
        rows, cols = len(grid), len(grid[0])
        # counter = 0
        def dfs(r, c):
            if (r < 0 or c < 0) or (r >= rows or c >= cols) or (r,c) in path or (grid[r][c] == 0):
                return 0
            path.add((r,c))
            return (1 + dfs(r + 1, c) +
                    dfs(r - 1, c) +
                    dfs(r , c + 1) +
                    dfs(r, c - 1) )
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in path:
                    res = max(dfs(r, c), res)
        return res
