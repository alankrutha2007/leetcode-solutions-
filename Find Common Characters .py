class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr = []
        for i in set(words[0]):
            count = min(word.count(i) for word in words)
            for _ in range(count):
                arr.append(i)
        return arr
