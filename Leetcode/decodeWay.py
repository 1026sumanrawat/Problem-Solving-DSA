# https://leetcode.com/problems/decode-ways/submissions/1258429749/

class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dp(i, memo):
            if i in memo:
                return memo[i]
            
            if s[i] == "0":
                return 0
            
            if i >= len(s)-1:
                return 1

            res = dp(i + 1 , memo)
            if int(s[i:i+2]) <= 26:
                res += dp(i + 2, memo)
            memo[i] = res
            return memo[i]
        return dp( 0, memo = {len(s): 1})
