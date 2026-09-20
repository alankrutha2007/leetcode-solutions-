class Solution:
    def averageValue(self, nums: list[int]) -> int:
        arr=[]
        for num in nums:
            if num%6==0:
                arr.append(num)
        if len(arr) == 0:
            return 0
        return sum(arr)//len(arr)       
