class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c=0
        bs=0
        for ch in s:
            if ch=="R":
                c+=1
            else:
                c-=1
            if c==0:
                bs+=1
        return bs
