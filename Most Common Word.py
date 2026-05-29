class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
       
        paragraph = paragraph.lower()

       
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        words = paragraph.split()

        freq = {}

        
        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1

        maximum = 0
        ans = ""

        
        for word in freq:
            if freq[word] > maximum:
                maximum = freq[word]
                ans = word

        return ans
