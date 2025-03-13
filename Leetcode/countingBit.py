# https://leetcode.com/problems/counting-bits/?envType=problem-list-v2&envId=xi4ci4ig

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        while n >= 0:
            binary_string = bin(n)
            res.append(binary_string.count('1'))
            n -= 1
        return res[::-1]
