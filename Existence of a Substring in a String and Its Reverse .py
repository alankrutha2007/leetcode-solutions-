class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev=s[::-1]
        for i in range(len(s)-1):
            substring=s[i:i+2]
            if substring in rev:
                return True
        return False   
