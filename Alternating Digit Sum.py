class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        total = 0
        sign = 1  
        for digit in s:
            total += int(digit) * sign
            sign *= -1   
        return total  
