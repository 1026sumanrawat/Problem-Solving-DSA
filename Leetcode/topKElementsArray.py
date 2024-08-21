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


# o(n) solution below

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
