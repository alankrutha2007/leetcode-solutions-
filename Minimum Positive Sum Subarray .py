class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if l <= j-i+1 <= r:
                    sums = sum(nums[i:j+1])
                    if sums > 0:
                        ans.append(sums)
        if len(ans) == 0:
            return -1
        return min(ans)
