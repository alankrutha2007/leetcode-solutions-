class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set()
        for ch in word:
            if ch.islower():
                if ch.upper() in word:
                    s.add(ch)
        return len(s)
