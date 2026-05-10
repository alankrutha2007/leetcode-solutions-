import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        arr=[]
        ans=[]
        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            arr.append((idx, -val))
        arr.sort()
        for idx,val in arr:
            ans.append(val)
        return ans
