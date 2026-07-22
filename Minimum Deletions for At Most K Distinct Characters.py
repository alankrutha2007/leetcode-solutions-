class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = Counter(s)
        if len(freq) <= k:
            return 0
        counts = list(freq.values())
        counts.sort()
        deletions = 0
        extra = len(freq) - k
        for i in range(extra):
            deletions += counts[i]
        return deletions   
