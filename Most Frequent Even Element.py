class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num, 0) + 1
        ans = -1
        max_freq = 0

        for num in freq:
            if freq[num] > max_freq:
                max_freq = freq[num]
                ans = num
            elif freq[num] == max_freq:
                ans = min(ans, num)

        return ans
