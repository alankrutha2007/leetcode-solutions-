class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num=bin(n)[2:]
        x=(1<<len(num))-1
        return n^x       
        
