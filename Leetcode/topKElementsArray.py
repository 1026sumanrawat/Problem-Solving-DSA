# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = k
        freq = dict(collections.Counter(nums))
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        res = []
        for key in freq.keys():
            if x == 0:
                return res
            res.append(key)
            x -= 1
        return res
