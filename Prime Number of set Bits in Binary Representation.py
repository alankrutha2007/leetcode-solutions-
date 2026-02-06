class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def prime(num):
            if(num<=1):
                return False
            for i in range(2,num):
                if(num%i==0):
                    return False
            return True   
        count=0
        for n in range(left,right+1):
            bits=bin(n).count('1')
            if prime(bits):
                count+=1
        return count     
