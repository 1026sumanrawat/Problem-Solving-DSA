# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                if temp.copy() not in res:
                    res.append(temp.copy())
                return
            temp.append(nums[i])
            dfs(i+1)
            temp.pop()
            dfs(i+1)
            
        dfs(0)
        return res
