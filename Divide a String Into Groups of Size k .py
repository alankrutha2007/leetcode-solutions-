class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        arr=[]
        n=len(s)
        for i in range(0,n,k):
            x=s[i:i+k]
            y=len(x)
            if y<k:
                x+=fill*(k-y)
            arr.append(x)
        return arr
