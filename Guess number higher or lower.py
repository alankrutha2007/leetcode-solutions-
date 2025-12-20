class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        high=n
        while(low<=high):
            mid=(low+high)//2
            g=guess(mid)
            if(g==0):
                return mid
            elif(g==1):
                low=mid+1
            elif(g==-1):
                high=mid-1
