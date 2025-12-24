class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list=[]
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                if(j==0 or j==i):
                    temp.append(1)
                else:
                    temp.append(list[i-1][j-1]+list[i-1][j])
            list.append(temp)
        return list
