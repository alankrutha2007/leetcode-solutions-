class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)
        d = {}          
        for i in range(len(s)):
            if s[i] in vowels:
                d[i] = s[i]
        rev = list(d.values())[::-1]
        j = 0
        for index in d:
            s[index] = rev[j]
            j += 1

        return "".join(s)   
