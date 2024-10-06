# 

# O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# Optimized O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffMap:
                return [diffMap[diff], i]
            else:
                diffMap[n] = i