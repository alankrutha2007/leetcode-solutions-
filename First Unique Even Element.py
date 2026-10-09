class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        arr=set()
        for num in nums:
            if num%2==0 and nums.count(num)==1:
                arr.add(num)
                if num in arr:
                    return num   
        if len(arr)==0:
            return -1
             
