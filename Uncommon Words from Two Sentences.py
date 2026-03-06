class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words=(s1 + " " + s2).split()
        result=[]
        for ch in words:
            if(words.count(ch)==1):
                result.append(ch)
        return result
