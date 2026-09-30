class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        n=len(nums)
        sums=set()
        for i in range(n - 1):
            s = nums[i] + nums[i + 1]
            if s in sums:
                return True
            sums.add(s)
        return False
