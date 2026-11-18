 class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        c=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]==nums[j]==nums[k] and j-i==k-j and nums.count(nums[i])==3:
                        c+=1
        return c
