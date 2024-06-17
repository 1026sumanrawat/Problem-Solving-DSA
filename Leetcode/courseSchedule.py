# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}
        for pre, crs in prerequisites:
            preMap[crs].append(pre)
        
        visitedSet = set()
        def dfs(crs):
            if crs in visitedSet:
                return False
            preq = preMap[crs]
            if preq == []:
                return True
            else:
                visitedSet.add(crs)
                for p in preq:
                    if not dfs(p):
                        return False
                visitedSet.remove(crs)
                preMap[crs] = []
            return True
        for num in range(numCourses):
            if not dfs(num): return False
        return True
