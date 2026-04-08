class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        total=0
        for i in count:
            if(count[i]==1):
                total+=i
        return total
