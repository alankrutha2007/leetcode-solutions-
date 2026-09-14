class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_range = -1
        ans = 0
        for n in nums:
            digits = []
            for d in str(n):
                digits.append(int(d))
            digit_range = max(digits) - min(digits)
            if digit_range > max_range:
                max_range = digit_range
                ans = n
            elif digit_range == max_range:
                ans += n
        return ans
