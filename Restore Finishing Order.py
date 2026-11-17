class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans=[]
        for IDs in order:
            if IDs in friends:
                ans.append(IDs)
        return ans
