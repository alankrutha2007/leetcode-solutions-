import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:     
        heap=[]
        for i,s in enumerate(score):
            heapq.heappush(heap,(-s,i))
        ans=[" "]*len(score)
        rank=1
        while heap:
            _,index=heapq.heappop(heap)
            if(rank==1):
                ans[index]="Gold Medal"
            elif(rank==2):
                ans[index]="Silver Medal"
            elif(rank==3):
                ans[index]="Bronze Medal"
            else:
                ans[index]=str(rank)
            rank+=1
        return ans
