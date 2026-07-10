class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        temp=""
        if len(temp)>len(s):
            return False
        for word in words:
            temp+=word
            if temp==s:
                return True
        return False
