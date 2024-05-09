class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def dfs(i, temp, sums):
            if sums == 0:
                res.append(temp.copy())
                return
            elif sums < 0 or i >= len(candidates):
                return
            else:
                temp.append(candidates[i])
                dfs(i, temp, sums-candidates[i])
                temp.pop()
                dfs(i+1, temp, sums)

        dfs(0,temp, target)
        return res
