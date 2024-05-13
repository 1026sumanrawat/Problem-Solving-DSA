# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        path = set()
        rows , cols = len(grid), len(grid[0])
        counter = 0
        def dfs(r, c ):
            if (r < 0 or c < 0) or (r >= rows or c >= cols) or (r,c) in path or grid[r][c] == "0":
                return
            path.add((r,c))
            res = dfs(r + 1, c) or dfs(r - 1, c) or dfs(r , c + 1) or dfs(r , c - 1)
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in path:
                    dfs(r, c)
                    counter += 1
        return counter
         
