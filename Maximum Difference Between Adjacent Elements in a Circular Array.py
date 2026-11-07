class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maximum=0
        for i in range(len(nums)):
            j=(i+1)%len(nums)
            diff=abs(nums[i]-nums[j])
            if diff>maximum:
                maximum=diff
        return maximum
