    class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min=sum(nums)%k
        return min

