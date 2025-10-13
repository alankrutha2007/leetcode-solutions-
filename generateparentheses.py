class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def generate(curr_str,open,close):
            if(open==n and close==n):
                ans.append(curr_str)
                return
            if(open<n):
                generate(curr_str+"(",open+1,close)
            if(close<open):
                generate(curr_str+")",open,close+1)
        generate("",0,0)
        return ans

   
