class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        num=set(nums)
        if original not in num:
            return original
        else:
            while original in num:
                original=original*2
        return original
