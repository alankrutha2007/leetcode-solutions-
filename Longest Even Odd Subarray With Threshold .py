class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_len = 0
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                count = 1
                for j in range(i+1, n):
                    if nums[j] <= threshold and nums[j] % 2 != nums[j-1] % 2:
                        count += 1
                    else:
                        break
                max_len = max(max_len, count)
        return max_len
