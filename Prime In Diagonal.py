class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n=len(nums)
        arr=[]
        max_prime=0
        for i in range(n):
            for j in range(n):
                if i==j or j==n-i-1:
                    arr.append(nums[i][j])  
        for num in arr:
            if num < 2:
                continue
            prime = True
            for k in range(2, int(num ** 0.5) + 1):
                if num % k == 0:
                    prime = False
                    break
            if prime:
                max_prime = max(max_prime, num)
        return max_prime 
