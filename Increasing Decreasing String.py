from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        ans = []
        while len(ans) < len(s):
            # Smallest to largest
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if count[ch] > 0:
                    ans.append(ch)
                    count[ch] -= 1
            # Largest to smallest
            for ch in "zyxwvutsrqponmlkjihgfedcba":
                if count[ch] > 0:
                    ans.append(ch)
                    count[ch] -= 1
        return "".join(ans)   
