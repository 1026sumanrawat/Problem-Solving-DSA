# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        totalJumps = 0
        window = 0
        lastIndexJump = 0
        destination = len(nums) - 1
        for i in range(len(nums)):
            window = max(window, i + nums[i])
            if i == lastIndexJump:
                lastIndexJump = window
                totalJumps += 1
                if window == destination:
                    return totalJumps
        return totalJumps
