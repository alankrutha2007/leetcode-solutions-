class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) == 2:
                if nums.index(nums[i]) == i:
                    ans = ans ^ nums[i]
        return ans
