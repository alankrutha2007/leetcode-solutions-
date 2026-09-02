class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        arr = nums[:]
        i = 0
        n = len(arr)
        while i < n:
            j = i
            while j < n and arr[j].bit_count() == arr[i].bit_count():
                j += 1
            arr[i:j] = sorted(arr[i:j])
            i = j
        return arr == sorted(nums)    
