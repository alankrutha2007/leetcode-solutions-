class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        arr=set()
        for num in nums:
            if num in arr:
                return num
            arr.add(num)
