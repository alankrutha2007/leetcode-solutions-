class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set()
        repeat=0
        miss=0
        for i in nums: 
            if i in s:
                repeat=i
            s.add(i)
        for i in range(1,len(nums)+1):
            if i not in nums:
                miss=i
        return [repeat,miss]
