class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        arr = set()
        total = 0
        for num in nums:
            count = nums.count(num)
            if count % k == 0 and num not in arr:
                total += num * count
                arr.add(num)
        return total
