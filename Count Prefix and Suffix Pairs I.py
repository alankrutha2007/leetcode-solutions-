class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        c = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) <= len(words[j]):
                    if words[j][:len(words[i])] == words[i] and words[j][-len(words[i]):] == words[i]:
                        c += 1
        return c
