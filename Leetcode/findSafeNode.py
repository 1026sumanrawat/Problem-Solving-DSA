# https://leetcode.com/problems/find-eventual-safe-states/description/?envType=daily-question&envId=2025-01-24

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        state = [0] * len(graph)
        safe = []

        def dfs(node):
            if state[node] > 0:
                return state[node] == 2
            
            state[node] = 1
            
            for neighbor in graph[node]:
                if state[neighbor] == 1 or not dfs(neighbor):
                    return False
            state[node] = 2
            return True

        for i in range(len(graph)):
            if dfs(i):
                safe.append(i)
        return safe
