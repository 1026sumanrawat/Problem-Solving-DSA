# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh, time = 0, 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [[0, 1], [1, 0], [ -1, 0], [0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                x,y = q.popleft()
                for dx, dy in directions:
                    newX = x + dx
                    newY = y + dy
                    if (newX < 0 or newX == rows) or (newY < 0 or newY == cols) or (grid[newX][newY] != 1) :
                        continue
                    grid[newX][newY] = 2
                    q.append((newX, newY))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
