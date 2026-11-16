class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        ans=[]
        for i in range(len(arr)):
            for j in range(len(pieces)):
                if arr[i]==pieces[j][0]:
                    ans+=pieces[j]
                    break
        if arr==ans:
            return True
        return False
