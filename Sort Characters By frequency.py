import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        heap=[]
        ans=[]
        for ch in freq:
            heapq.heappush(heap, (-freq[ch], ch))
        while(len(heap)>0):
            f, ch = heapq.heappop(heap)
            ans.append(ch*(-f))
        return ''.join(ans)
