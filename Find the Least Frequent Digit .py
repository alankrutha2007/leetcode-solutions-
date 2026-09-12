class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s = str(n)
        least = 100
        ans = 0
        for digit in s:
            frequency = s.count(digit)
            if frequency < least:
                least = frequency
                ans = int(digit)
            elif frequency == least:
                ans = min(ans, int(digit))
        return ans
