class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for num in nums:
           x=0
           for digit in str(num):
            x+=int(digit)
           arr.append(x)
        res=sorted(arr)
        return res[0]
