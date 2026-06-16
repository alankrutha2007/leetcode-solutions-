class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d={}
        alphabet="abcdefghijklmnopqrstuvwxyz"
        i=0
        for ch in key:
            if ch!=" " and ch not in d:
                d[ch]=alphabet[i]
                i+=1
        ans=""
        for ch in message:
            if ch==" ":
                ans+=" "
            else:
                ans+=d[ch]
        return ans
