class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}  # stores last index of each number
        for i, num in enumerate(nums):
            if num in last_index:
                if i - last_index[num] <= k: # check if difference is <= k
                    return True
            last_index[num] = i # update index of current number
        return False


        
