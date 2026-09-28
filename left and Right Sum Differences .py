class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(0,n):
            leftSum=0
            rightSum=0
            for j in range(i):
                leftSum+=nums[j]
            for j in range(i+1,n):
                rightSum+=nums[j]
            ans.append(abs(leftSum-rightSum))
        return ans
