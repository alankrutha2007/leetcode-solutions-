class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if(word[i]==ch):
                prefix=word[:i+1]
                rest=word[i+1:]
                return prefix[::-1]+rest
        return word
