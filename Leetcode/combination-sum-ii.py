# https://leetcode.com/problems/combination-sum-ii/description/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        candidates.sort()
        def dfs(sums, i):
            if sums == 0:
                if temp not in res:
                    res.append(temp.copy())
                return
            if sums < 0 or i >= len(candidates):
                return
            ele = candidates[i]
            temp.append(candidates[i])
            dfs(sums - candidates[i], i+1)
            temp.pop()
            index = 1
            while index + i < len(candidates) and candidates[index+i] == ele:
                index += 1
            dfs(sums, i+index)
        dfs(target, 0)
        return res
