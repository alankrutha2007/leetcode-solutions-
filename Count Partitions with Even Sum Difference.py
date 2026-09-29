class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n-1):
            LeftSubarray=0
            RightSubarray=0
            for j in range(i+1):
                LeftSubarray+=nums[j]
            for j in range(i+1,n):
                RightSubarray+=nums[j]
            if (LeftSubarray-RightSubarray)%2==0:
                c+=1
        return c
