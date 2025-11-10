class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return text == text[::-1]
