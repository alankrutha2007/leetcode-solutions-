class Solution:
    def countPrimes(self, n: int) -> int:
        prime=[1]*n
        for index in range(2,int(n**0.5)+1):
            if(prime[index]==1):
                for j in range(index*index,n,index):
                    prime[j]=0
        c=0
        for i in range(2,n):
            if(prime[i]==1):
                c+=1
        return(c)
        
