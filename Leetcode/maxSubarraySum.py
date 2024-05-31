# https://leetcode.com/problems/maximum-subarray/description/
#  Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        currSum = 0
        for num in nums:
            currSum += num
            maxi = max(currSum, maxi)
            if currSum < 0:
                currSum = 0
        return maxi
