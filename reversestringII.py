class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list=list(s)
        for i in range(0,len(s),2*k):
            if(i+k>len(s)):
                s_list[i:]=s_list[i:][::-1]
            else:
                s_list[i:i+k]=s_list[i:i+k][::-1]
        return "".join(s_list)          
        
