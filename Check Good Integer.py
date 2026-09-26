class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_Sum=0
        square_Sum=0
        for digit in str(n):
            digit_Sum+=int(digit)
            square_Sum+=int(digit)**2
        if square_Sum-digit_Sum>=50:
            return True
        return False 
