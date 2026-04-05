class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total=0
        for word in words:
            temp=list(chars)
            exist=True
            for ch in word:
                if ch in temp:
                    temp.remove(ch)
                else:
                    exist=False
                    break
            if(exist):
                total+=len(word)
        return total       
