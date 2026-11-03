class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            ans+=max(nums)-num
        return ans
