# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(arr, i, memo):
            if i >= len(arr) :
                return 0
            if i in memo:
                return memo[i]
            a = arr[i] + dp(arr, i + 2, memo)
            b = dp(arr, i + 1, memo)
            memo[i] = max(a,b)
            return memo[i]

        if len(nums) <= 2:
            return max(nums)
        memo = {}
        x = dp(nums, 0, memo)
        return x
