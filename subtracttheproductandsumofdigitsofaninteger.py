class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x,y=1,0
        for digit in str(n):
            d = int(digit)
            x=x*d
            y=y+d
        return x-y

        
