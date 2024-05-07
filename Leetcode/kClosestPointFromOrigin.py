#973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for point in points:
            dist = math.sqrt((point[0] * point[0]) + (point[1] * point[1]))
            heapq.heappush(maxheap, (-dist, point[0], point[1]))
        while len(maxheap) > k:
            heapq.heappop(maxheap)
        return [(x,y) for (dist,x,y) in maxheap]
