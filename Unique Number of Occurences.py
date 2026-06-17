from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence=Counter(arr)
        if len(occurence.values())==len(set(occurence.values())):
            return True
        return False
