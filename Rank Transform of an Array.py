class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank={}
        sorted_arr=sorted(set(arr))
        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]]=i+1
        ans=[]
        for num in arr:
            ans.append(rank[num])
        return ans      
