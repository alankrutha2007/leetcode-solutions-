class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dict={}
        for a,b in paths:
            dict[a]=b
        for a,b in paths:
            if b not in dict:
                return b
