import heapq
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap=[]
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            for j in range(min(limits[i], len(grid[i]))):
                heapq.heappush(heap, -grid[i][j])
        ans = 0
        while heap and k > 0:
            ans += -heapq.heappop(heap)
            k -= 1
        return ans
