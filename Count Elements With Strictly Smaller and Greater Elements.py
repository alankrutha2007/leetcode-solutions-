class Solution:
    def countElements(self, nums: List[int]) -> int:
        large=max(nums)     
        small=min(nums)
        c=0
        for num in nums:
            if small<num<large:
                c+=1
        return c
