from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words) #count frequency
        heap=[]
        ans=[]
        for word,freq in count.items(): #build heap
            heapq.heappush(heap,(-freq,word))
        for _ in range(k): #pop k elements
            freq,word=heapq.heappop(heap)
            ans.append(word)
        return ans
