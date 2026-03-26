class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        x=int(str(num)[::-1])
        y=int(str(x)[::-1])
        return num==y
