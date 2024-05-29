# https://leetcode.com/problems/coin-change/submissions/1270891387/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp( targetsum, numbers, memo):
            if targetsum in memo:
                return memo[targetsum]
            if targetsum == 0:
                return []
            if targetsum < 0: 
                return None
            shortestComb = None
            for num in numbers:
                rem = targetsum - num
                temp = dp(rem, numbers, memo)
                if temp is not None:
                    newtemp = temp.copy()
                    newtemp.append(num)
                    if shortestComb is None:
                        shortestComb = newtemp
                    if  len(shortestComb) > len(newtemp):
                        shortestComb = newtemp
            memo[targetsum] = shortestComb
            return shortestComb
        memo = {}
        
        v = dp(amount, coins, memo)
        return -1 if v is None else len(v)
