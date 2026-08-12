class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum=0
        total=sum(nums)
        for i in range(len(nums)):
            curr_element=nums[i]
            right_sum=total-left_sum-curr_element
            if left_sum==right_sum:
                return i
            else:
                left_sum+=curr_element
        return -1
