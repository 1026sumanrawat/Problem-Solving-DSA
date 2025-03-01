#  https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for i in reversed(range(len(digits))):
            sums = digits[i] + carry
            if sums > 9:
                res.append(sums%10)
                carry = 1
            else:
                res.append(sums)
                sums = 0
                carry = 0
        if carry == 1:
            res.append(carry)
        return res[::-1]
