# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(arr, i, memo):
            if i >= len(arr):
                return 0
            if i in memo:
                return memo[i]
            x = arr[i] + dp(arr, i + 2, memo)
            y = dp(arr, i + 1, memo)
            memo[i] = max(x,y)
            return memo[i]

        if len(nums) <= 2:
            return max(nums)
        memo1 = {}
        memo2 = {}
        y = dp(nums[:len(nums)-1], 0, memo1)
        x = dp(nums[1:], 0, memo2)
        return max(x,y)
