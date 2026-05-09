import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]
        ans=[]
        arr=[]
        for i in range(len(mat)):
            arr.append([mat[i].count(1),i])
        for i in range(len(arr)):
            heapq.heappush(heap,arr[i])
        while(k>len(ans)):
            x=heapq.heappop(heap)
            ans.append(x[1])
        return ans
