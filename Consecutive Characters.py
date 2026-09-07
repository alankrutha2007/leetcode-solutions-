class Solution:
    def maxPower(self, s: str) -> int:
        c=1
        ans=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                c=1
            ans=max(c,ans)
        return ans
