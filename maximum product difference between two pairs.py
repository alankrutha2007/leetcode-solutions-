class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        pair1=nums[n-1]*nums[n-2] #largest pair
        pair2=nums[0]*nums[1] #smallest pair
        return pair1-pair2
