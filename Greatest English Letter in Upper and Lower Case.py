class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = ""
        for ch in s:
            if ch.islower() and ch.upper() in s:
                if ch.upper() > ans:
                    ans = ch.upper()
        return ans
