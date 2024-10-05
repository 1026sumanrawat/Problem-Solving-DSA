# https://leetcode.com/problems/decode-ways/submissions/1258429749/
# Useful links: https://www.youtube.com/watch?v=HW-y3gvQTVQ
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

# 2nd solution similar approach
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.solve(0, s, memo)
        
    def solve(self, i, s, memo):
        if s[i:] in memo:
            return memo[s[i:]]
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0
        
        memo[s[i:]] = self.solve(i+1, s, memo)
        if i+1 < len(s):
            if int(s[i:i+2]) <=26 and int(s[i:i+2]) >= 10:
                memo[s[i:]] += self.solve(i+2, s, memo)
        return memo[s[i:]]
