class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def backtracking(i):
            if i >= len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[i])
            backtracking(i+1)

            temp.pop()
            backtracking(i+1)
        backtracking(0)
        return res
                
