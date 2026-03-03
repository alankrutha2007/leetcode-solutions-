class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = max(nums)   
        i = nums.index(max1)  
        for n in nums:
            if(n!=max1 and max1<2 * n):
                return -1
        return i
