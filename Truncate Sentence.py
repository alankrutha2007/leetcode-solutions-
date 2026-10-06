class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x=s.split()
        return " ".join(x[0:k])
