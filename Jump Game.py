class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex=0
        n=len(nums)
        for i in range(0,n):
            if(i>maxIndex):
                return False
            if(nums[i]+i>maxIndex):
                maxIndex=nums[i]+i
        return True
