class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        if len(diff) == 0:
            return True
        if len(diff) != 2:
            return False
        i = diff[0]
        j = diff[1]
        if s1[i] == s2[j] and s1[j] == s2[i]:
            return True
        return False
