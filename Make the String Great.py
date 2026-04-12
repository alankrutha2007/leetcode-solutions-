class Solution:
    def makeGood(self, s: str) -> str:
        result=[]
        for ch in s:
            if(len(result)>0 and result[-1].islower()!=ch.islower() and result[-1].lower()==ch.lower()):
                result.pop()
            else:
                result.append(ch)
        return "".join(result)
