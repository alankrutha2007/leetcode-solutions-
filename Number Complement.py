class Solution:
    def findComplement(self, num: int) -> int:
        n=bin(num)[2:]
        x=(1<<len(n))-1
        complement=(~num)&x
        return complement    
