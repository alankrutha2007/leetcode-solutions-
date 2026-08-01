class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        curr = word
        ans = 0
        while curr in sequence:
            ans += 1
            curr += word
        return ans
