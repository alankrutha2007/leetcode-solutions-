class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            smallest = min(nums)
            index = nums.index(smallest)
            nums[index] = -nums[index]
        return sum(nums)
