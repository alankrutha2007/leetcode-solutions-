class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        score = 0
        for _ in range(k):
            m = -heapq.heappop(heap)
            score += m
            heapq.heappush(heap, -(m + 1))
        return score
