class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []
        for ch in s:
            if ch.isdigit():
                digits.append(int(ch))
        digits = list(set(digits))
        digits.sort(reverse=True)
        if len(digits) >= 2:
            return digits[1]
        else:
            return -1
