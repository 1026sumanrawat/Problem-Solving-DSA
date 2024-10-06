# https://leetcode.com/problems/maximum-product-subarray/submissions/1413110245/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd1 = float('-inf')
        maxProd2 = float('-inf')
        prod = 1

        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                prod = 1
                if maxProd1 < 0:
                    maxProd1 = 0
            else:
                prod = prod * num
                if prod > maxProd1:
                    maxProd1 = prod
        prod = 1
        for i in range(len(nums)-1, 0, -1):
            num = nums[i]
            if num == 0:
                prod = 1
                if maxProd1 < 0:
                    maxProd1 = 0
            else:
                prod = prod * num
                if prod > maxProd2:
                    maxProd2 = prod
        return max(maxProd1, maxProd2)
                
