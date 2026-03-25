class Solution:
    def maxProduct(self, n: int) -> int:
        digits=[]
        for i in str(n):
            digits.append(int(i))
        digits.sort()
        return digits[-1]*digits[-2]
