# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1414119592/
# t(n) = O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        sub = set()
        
        for right in range(len(s)):
            if s[right] not in sub:
                sub.add(s[right])
                maxLen = max(maxLen, len(sub))
            else:
                while s[right] in sub:
                    sub.remove(s[left])
                    left += 1
                sub.add(s[right])
        return maxLen
