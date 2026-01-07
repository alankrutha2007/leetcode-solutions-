class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        temp=0
        for num in range(left,right+1):
            temp=num
            self_dividing=True
            while(temp>0):
                digit=temp%10
                if(digit==0 or num%digit!=0):
                    self_dividing=False
                    break
                temp//=10
            if(self_dividing):
                result.append(num)
        return result
