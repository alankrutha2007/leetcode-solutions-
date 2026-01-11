class Solution:
    def reverseBits(self, n: int) -> int:
        bin=format(n,'032b')
        rev_bin=bin[::-1]
        return int(rev_bin,2)   
