class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans=set()
        for ch in s:
            if ch in ans:
                return ch
            ans.add(ch)
