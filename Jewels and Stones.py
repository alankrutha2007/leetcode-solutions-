class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x=set(jewels)
        count=0
        for ch in stones:
            if ch in x:
                count+=1
        return count    
