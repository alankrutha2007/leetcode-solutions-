class Solution:
    def findGCD(self, nums: List[int]) -> int:
        large=max(nums)
        small=min(nums)
        return gcd(large,small)  
