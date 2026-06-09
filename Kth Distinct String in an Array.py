class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        ans=[]
        for word in arr:
            d[word] = d.get(word, 0) + 1
        for word in arr:
            if d[word] == 1:
                ans.append(word)
        if(len(ans)>=k):
            return ans[k-1]
        else:
            return ""
