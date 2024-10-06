# https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1414160632/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        freqMap = {}
        left = 0
        for right in range(len(s)):
            freqMap[s[right]] = 1 + freqMap.get(s[right], 0)

            if (right -left + 1) - max(freqMap.values()) <= k:
                maxLen = max(maxLen, (right -left + 1))
            else:
                freqMap[s[left]] = freqMap.get(s[left]) - 1
                left += 1
        return maxLen
