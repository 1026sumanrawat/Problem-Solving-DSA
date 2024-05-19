# https://leetcode.com/problems/task-scheduler/submissions/1262031987/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        while q or maxHeap:
            time += 1
            if maxHeap:
                ele = 1 + heapq.heappop(maxHeap)
                if ele:
                    q.append((ele, time + n))

            if q and q[0][1] == time :
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

            

        
