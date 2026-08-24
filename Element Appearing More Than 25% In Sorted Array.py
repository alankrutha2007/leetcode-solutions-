class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        for i in arr:
            if arr.count(i)>n//4:
                return i
