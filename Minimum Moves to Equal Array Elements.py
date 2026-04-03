class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=len(nums)
        moves=sum(nums)-(n*min(nums))
        return moves
