class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if i % 2 == 0:
                expected = '0'
            else:
                expected = '1'

            if s[i] != expected:
                count += 1
        return min(count, len(s) - count)
