class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}

        
        for num in arr:
            d[num] = d.get(num, 0) + 1

        ans = -1

        for num in d:
            if d[num] == num:
                ans = max(ans, num)

        return ans        
