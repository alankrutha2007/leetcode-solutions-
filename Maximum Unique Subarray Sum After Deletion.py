class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        total = 0
        arr=[]
        for num in nums:
            if num > 0 and num not in arr:
                total+=num
                arr.append(num)
        return total
