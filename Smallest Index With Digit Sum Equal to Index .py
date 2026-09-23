class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=0
            for digit in str(nums[i]):
                x+=int(digit)
            if i==x:
                return i
        return -1
        
