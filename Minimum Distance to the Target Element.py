class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        distances=[]
        for i in range(len(nums)):
            if(nums[i]==target):
                distances.append(abs(i-start))
        return min(distances)
