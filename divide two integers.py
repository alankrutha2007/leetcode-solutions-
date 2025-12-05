class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative=(dividend < 0)^(divisor < 0)
        dividend=abs(dividend)
        divisor=abs(divisor)
        quotient=0
        while(dividend>=divisor):
            dividend-=divisor
            quotient+=1
        if(negative):
            return -quotient
        else:
            return quotient

        
