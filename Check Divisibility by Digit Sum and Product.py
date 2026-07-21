class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp=n
        Sum=0
        Product=1
        while temp>0:
            digit=temp%10
            Sum+=digit
            Product*=digit
            temp=temp//10
        total=Sum+Product
        if n%total==0:
            return True
        return False
