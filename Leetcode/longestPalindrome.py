# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            l , r = i , i
            sub = ""
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if l == r:
                        sub = s[i]
                    else:
                        sub = s[l] + sub + s[r]
                else:
                    break    
                l -= 1
                r += 1
            res.append(sub)
        for i in range(len(s)):
            l , r = i , i + 1
            sub = ""
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    sub = s[l] + sub + s[r]
                else:
                    break
                l -= 1
                r += 1
            res.append(sub)
        return max(res, key = len)
            
