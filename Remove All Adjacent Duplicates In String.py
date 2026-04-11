class Solution:
    def removeDuplicates(self, s: str) -> str:
        result=[]
        for ch in s:
            if(result and result[-1]==ch):
                result.pop()
            else:
                result.append(ch)
        return ''.join(result)
