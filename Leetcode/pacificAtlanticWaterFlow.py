# https://leetcode.com/problems/pacific-atlantic-water-flow/
# reference https://www.youtube.com/watch?v=krL3r7MY7Dc

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        pacific = [[None for _ in range(cols)] for _ in range(rows)]
        atlantic = [[None for _ in range(cols)] for _ in range(rows)]
        
        def dfs(r, c, prev, ocean):
            if (r < 0 or c < 0) or (r >= rows or c >= cols):
                return
            if  heights[r][c] < prev or ocean[r][c]:
                return 
            ocean[r][c] = True
            dfs( r + 1, c, heights[r][c],ocean)
            dfs( r - 1, c, heights[r][c],ocean)
            dfs( r , c + 1, heights[r][c],ocean)
            dfs( r , c - 1, heights[r][c], ocean)
            return 

        # DFS
        for i in range(cols):
            dfs(0, i, float('-inf'), pacific)
            dfs(rows-1, i, float('-inf'), atlantic)

        for j in range(rows):
            dfs(j, cols-1, float('-inf'), atlantic)
            dfs(j, 0, float('-inf'), pacific)

        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])
        return res

            
