class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=set(allowed)
        count=0
        for word in words:
            consistent=True
            for ch in word:
                if ch not in s:
                    consistent=False
            if consistent:
                count+=1
        return count      
