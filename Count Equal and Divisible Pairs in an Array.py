class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        c=0
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (i*j)%k==0:
                    c+=1  
        return c             
