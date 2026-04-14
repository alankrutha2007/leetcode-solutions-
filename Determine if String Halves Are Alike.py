class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels="aeiouAEIOU"
        mid=len(s)//2
        left=0
        for ch in s[:mid]:
            if ch in vowels:
                left+=1
        right=0
        for ch in s[mid:]:
            if ch in vowels:
                right+=1
        if(left==right):
            return True
        else:
            return False 
