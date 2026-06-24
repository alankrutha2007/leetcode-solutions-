class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans=[]
        arr.sort()
        min_diff=float('inf')
        for i in range(len(arr) - 1):
            min_diff = min(min_diff, arr[i + 1] - arr[i])
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == min_diff:
                ans.append([arr[i], arr[i + 1]])
        return ans
