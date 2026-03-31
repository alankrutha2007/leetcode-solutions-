class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr=set()
        duplicates=[]
        for i in nums:
            if i in arr:
                duplicates.append(i)
            else:
                arr.add(i)
        return duplicates
