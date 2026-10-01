class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums1=[]
        nums2=[]
        for i in range(len(nums)):
            if nums[i] not in nums1:
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])
        if len(set(nums1))==len(nums1) and len(set(nums2))==len(nums2):
            return True
        return False
