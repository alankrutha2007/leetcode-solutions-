class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result=[]
        height=sorted(heights,reverse=True)
        for i in height:
            index=heights.index(i)
            result.append(names[index])
        return result  
