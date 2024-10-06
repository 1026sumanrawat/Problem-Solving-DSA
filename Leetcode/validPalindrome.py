# https://leetcode.com/problems/valid-palindrome/submissions/1414167891/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = s.lower()
        right = len(lowerS) - 1
        left = 0
        while left < right:
            if not lowerS[left].isalnum():
                left += 1
                continue
            if not lowerS[right].isalnum():
                right -= 1
                continue
            if lowerS[left] != lowerS[right]:
                return False
            left += 1
            right -= 1

        return True
