# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # costs = 0
        def minCost(cost, n, memo):
            if n == len(cost)-1 or n == len(cost)-2:
                return cost[n]
            if n in memo:
                return memo[n]
            a = minCost(cost, n + 1, memo)
            b = minCost(cost, n + 2, memo)
            memo[n] = min(a,b) + cost[n]
            return memo[n]
        if len(cost) == 2:
                return min(cost[0], cost[1])
        memo = {}
        x = minCost(cost, 0, memo)
        y = minCost(cost, 1, memo)
        return min(x, y)

             

