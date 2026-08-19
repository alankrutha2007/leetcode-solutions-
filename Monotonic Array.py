class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        Increase=True
        Decrease=True
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                Increase=False
            if nums[i]>nums[i-1]:
                Decrease=False
        return Increase or Decrease
