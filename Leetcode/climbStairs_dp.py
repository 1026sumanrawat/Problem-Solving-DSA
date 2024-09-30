class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.dp(n, memo)

    def dp(self, n, memo):
        if n == 0 or n == 1:
                return 1
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.dp(n-1, memo) + self.dp(n-2, memo)
        return memo[n]
