class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate(index,subset):
            if(index==len(nums)):
                ans.append(subset.copy())
                return
            subset.append(nums[index])
            generate(index+1,subset)
            subset.pop()
            generate(index+1,subset)
        subset=[]
        ans=[]
        generate(0,[])
        return ans

    


        
