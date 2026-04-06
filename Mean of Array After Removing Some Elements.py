class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=len(arr)
        remove=n//20
        total=0
        count=0
        for i in range(remove,n-remove):
            total+=arr[i]
            count+=1
        return total/count
