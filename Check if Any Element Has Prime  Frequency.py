from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums):
        freq = Counter(nums)

        for count in freq.values():
            if self.isPrime(count):
                return True

        return False

    def isPrime(self, n):
        if n <= 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True
